from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
import os
import aiofiles

from controllers import DataController, ProjectController

data_router = APIRouter(
    prefix="/api/v1/data"
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id : str, file : UploadFile,
                      app_settings : Settings = Depends(get_settings)):
    
    # Validate uploaded file
    is_valid, signal = DataController().validation_upoladed_file(file=file)

    if not is_valid:
        return {
            "signal" : signal
        }
    project_dir_path = ProjectController().get_project_path(project_id = project_id)
    
    file_path = os.path.join(
        project_dir_path,
        file.filename
    )
    
    async with aiofiles.open(file_path, "wb") as f:
        while chunk := await file.read( app_settings.FILE_DEFAULT_CHUNK_SIZE ):
            await f.write(chunk)

    return {
        "signal" : signal
    }




