from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId
from pydantic_settings import SettingsConfigDict
from pymongo import IndexModel


class Project(BaseModel):
    id : Optional[ObjectId] = Field(None, alias="_id")
    project_id : str = Field(..., min_length = 1)

    model_config = SettingsConfigDict(
        env_file=".env",
        arbitrary_types_allowed = True,
        )

    @field_validator("project_id")
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError("project_id must be alphanumeric")

        return value
    
    @classmethod
    def get_indexes(cls):

        return [

            IndexModel( [ ("project_id", 1) ], name = "project_id_index_1", unique = True ),
            #     key ( or keys ) and asc or des in tuple      name for the index    should this key be unique                                    
            
        ] 
    

    
