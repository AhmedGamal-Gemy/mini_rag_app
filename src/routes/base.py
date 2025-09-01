from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix = "/api/v1", # Anything under this APIRouter should be wrote first /api/v1/anything

)

# We then use base_router as a decorator
@base_router.get('/')
async def welcome():
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')

    return {
        'app_name' : app_name,
        'app_version' : app_version
    }