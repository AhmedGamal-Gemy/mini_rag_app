from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId
from pydantic_settings import SettingsConfigDict

class Project(BaseModel):
    _id : Optional[ObjectId]
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

    
