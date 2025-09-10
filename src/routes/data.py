from fastapi import FastAPI, APIRouter, Depends, UploadFile, status,Request
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
import os
import aiofiles
from models import ResponseSignal
from controllers import DataController, ProjectController, ProcessController
from .schemes.data import ProcessingRequest
from models.ProjectDataModel import ProjectDataModel
from models.ChunkDataModel import ChunkDataModel
from models.db_schemes import Chunk
from bson.objectid import ObjectId

import logging

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data"
)

@data_router.post("/upload/{project_id}")
async def upload_data(request : Request, project_id : str, file : UploadFile,
                      app_settings : Settings = Depends(get_settings)):
    
    project_model = ProjectDataModel(
            db_client= request.app.db_client
        )
    
    project = await project_model.get_project_or_create_one(project_id = project_id)
    
    data_controller = DataController()

    # Validate uploaded file
    is_valid, signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            statuscode = status.HTTP_400_BAD_REQUEST,
            content = {
                "signal" : signal.value
            }
        )
        
    project_dir_path = ProjectController().get_project_path(project_id = project_id)
    
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )
    
    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read( app_settings.FILE_DEFAULT_CHUNK_SIZE ):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file : {e}")

        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                "signal" : ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )
    
    return JSONResponse(
            status_code = status.HTTP_200_OK,
            content = {
                "signal" : ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                "file_id" : file_id,
            }
        )

@data_router.post("/process/{project_id}")
async def process(request : Request ,project_id : str, process_request : ProcessingRequest): # A must to validate the request
    
    file_id = process_request.file_id
    chunk_size = process_request.chunk_size
    overlap_size = process_request.overlap_size
    do_reset = process_request.do_reset

    project_model = ProjectDataModel(
            db_client= request.app.db_client
        )
    chunk_model = ChunkDataModel(
            db_client= request.app.db_client
        )

    project = await project_model.get_project_or_create_one(project_id = project_id)

    process_controller = ProcessController( project_id )

    file_content = process_controller.get_file_content( file_id = file_id )

    file_chunks = process_controller.process_file_content(file_content= file_content, 
                                                          file_id = file_id, chunk_size = chunk_size, 
                                                          overlap_size=overlap_size)
    
    if file_chunks is None or len(file_chunks) == 0:
        return JSONResponse(
            statuscode = status.HTTP_400_BAD_REQUEST,
            content = {
                "signal" : ResponseSignal.PROCESSING_FAILED.value
            }
        )

    file_chunks_records = [
        Chunk(
            chunk_text = chunk.page_content,
            chunk_metadata = chunk.metadata,
            chunk_order = index+1,
            chunk_project_id = ObjectId(project.id),
        )
        for index, chunk in enumerate(file_chunks)
    ]

    if do_reset == 1:
        print("RESET IS 1")
        _ = await chunk_model.delete_chunks_by_project_id( project.id )

    no_records = await chunk_model.create_many_chunks(file_chunks_records)


    return JSONResponse(
        status_code= status.HTTP_201_CREATED,
        content= {
            "signal" : ResponseSignal.PROCESSING_SUCCESS.value,
            "inserted_chunks" : no_records  
        }
    )





    
