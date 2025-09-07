from pydantic import BaseModel, Field
from typing import Optional
from bson.objectid import ObjectId
from pydantic_settings import SettingsConfigDict

class Chunk(BaseModel):
    _id : Optional[ObjectId]
    
    chunk_text : str = Field(..., min_length = 1)
    chunk_metadata : dict
    chunk_order : int = Field(... , gt = 0)
    chunk_project_id : ObjectId

    model_config = SettingsConfigDict(
        env_file=".env",
        arbitrary_types_allowed = True,
        )
