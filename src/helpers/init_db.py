from helpers.config import get_settings
from pymongo import AsyncMongoClient
from models.db_schemes.project import Project
from models.db_schemes.chunk import Chunk
from models.enums.DatabaseEnums import DatabaseEnum


async def init_database():

    settings = get_settings()
    mongo_conn = AsyncMongoClient( settings.MONGODB_URL )
    db_client = mongo_conn[ settings.MONGODB_DATABASE ]
    
    await init_indexes(db_client)

    return mongo_conn, db_client

async def init_indexes(db_client : object):

    chunk_indexes = Chunk.get_indexes()

    chunks_collection = db_client[DatabaseEnum.COLLECTION_CHUNK_NAME.value]    
    await chunks_collection.create_indexes( chunk_indexes )


######################################################################################

    project_indexes = Project.get_indexes()

    project_collection = db_client[DatabaseEnum.COLLECTION_PROJECT_NAME.value]    
    await project_collection.create_indexes( project_indexes )