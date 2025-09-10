from .BaseDataModel import BaseDataModel
from .db_schemes import Chunk
from bson.objectid import ObjectId
from .enums.DatabaseEnums import DatabaseEnum
from pymongo import InsertOne


class ChunkDataModel(BaseDataModel):
    
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection = db_client[DatabaseEnum.COLLECTION_CHUNK_NAME.value]


    async def create_chunk(self, chunk : Chunk):
        
        result = await self.collection.insert_one( chunk.model_dump(by_alias=True, exclude_unset= True) )
        chunk._id = result.inserted_id

        return chunk
    
    async def get_chunk(self, chunk_id : str):

        result = self.collection.find_one({
            "_id" : ObjectId( chunk_id ) 
        })

        if result is None:
            return Chunk(**result)
        
    async def create_many_chunks(self, chunks : list, batch_size : int = 100):

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i : i + batch_size ]

        operations = [

            InsertOne( chunk.model_dump(by_alias=True, exclude_unset= True) ) for chunk in batch
        
        ]

        await self.collection.bulk_write( operations )
        
        return len(chunks)

    async def delete_chunks_by_project_id(self, project_id : ObjectId):
        print("PROJECT ID IS ", project_id)
        result = await self.collection.delete_many({
            "chunk_project_id" : project_id
        })

        return result.deleted_count

        


    