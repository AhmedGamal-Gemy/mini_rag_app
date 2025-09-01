from fastapi import FastAPI, APIRouter
import os
from helpers.config import get_settings, Settings

base_router = APIRouter(
    prefix = "/api/v1", # Anything under this APIRouter should be wrote first /api/v1/anything

)

# We then use base_router as a decorator
@base_router.get('/')
async def welcome():
    app_settings = get_settings()

    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION

    return {
        'app_name' : app_name,
        'app_version' : app_version
    }