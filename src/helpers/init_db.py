from helpers.config import get_settings
from pymongo import AsyncMongoClient
from models.db_schemes.project import Project
from models.db_schemes.chunk import Chunk
from models.db_schemes.asset import Asset
from models.enums.DatabaseEnums import DatabaseEnum



async def init_database():

    settings = get_settings()
    mongo_conn = AsyncMongoClient( settings.MONGODB_URL )
    db_client = mongo_conn[ settings.MONGODB_DATABASE ]
    
    await init_indexes(db_client)

    return mongo_conn, db_client

async def init_indexes(db_client : object):

    model_collection_map = {
        Chunk : DatabaseEnum.COLLECTION_CHUNK_NAME.value,
        Project : DatabaseEnum.COLLECTION_PROJECT_NAME.value,
        Asset : DatabaseEnum.COLLECTION_ASSET_NAME.value
    }

    for model, collection_name in model_collection_map.items():

        indexes = model.get_indexes()
        if indexes:
            collection = db_client[ collection_name ]
            await collection.create_indexes( indexes )


#     chunk_indexes = Chunk.get_indexes()

#     chunks_collection = db_client[DatabaseEnum.COLLECTION_CHUNK_NAME.value]    
#     await chunks_collection.create_indexes( chunk_indexes )


# ######################################################################################

#     project_indexes = Project.get_indexes()

#     project_collection = db_client[DatabaseEnum.COLLECTION_PROJECT_NAME.value]    
#     await project_collection.create_indexes( project_indexes )

# ############################################################################################

#     asset_indexes = Asset.get_indexes()

#     asset_collection = db_client[DatabaseEnum.COLLECTION_ASSET_NAME.value]    
#     await asset_collection.create_indexes( asset_indexes )