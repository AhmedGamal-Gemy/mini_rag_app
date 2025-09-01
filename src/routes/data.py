from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
import os

from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data"
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id : str, file : UploadFile,
                      app_settings : Settings = Depends(get_settings)):
    
    # Validate uploaded file
    is_valid, signal = DataController().validation_upoladed_file(file=file)

    return {
        "signal" : signal
    }
        




