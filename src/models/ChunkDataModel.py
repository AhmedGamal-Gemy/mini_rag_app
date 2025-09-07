from BaseDataModel import BaseDataModel
from .db_schemes import Chunk
from .enums.DatabaseEnums import DatabaseEnum


class ChunkDataModel(BaseDataModel):
    
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection = db_client[DatabaseEnum.COLLECTION_CHUNK_NAME.value]
    

    