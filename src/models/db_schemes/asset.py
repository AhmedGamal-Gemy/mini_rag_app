from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson.objectid import ObjectId
from pydantic_settings import SettingsConfigDict
from pymongo import IndexModel
from models.enums.ProcessingEnums import ProcessingEnums
from datetime import datetime, timezone
from models.enums.AssetTypesEnums import AssetTypeEnum

class Asset(BaseModel):

    # Fields
    id : Optional[ObjectId] = Field(None, alias="_id")
    asset_project_id : str
    asset_type : AssetTypeEnum
    asset_name : str = Field(... , min_length=1)
    asset_size : int = Field(gt = 0, default= None)
    asset_config : dict = Field(default = None)
    asset_created_at : datetime = Field( default= datetime.now(timezone.utc) )

    model_config = SettingsConfigDict(
        env_file=".env",
        arbitrary_types_allowed = True,
    )

    @classmethod
    def get_indexes(cls):
        return [

            IndexModel( [ ("asset_project_id", 1), ("asset_name", 1) ], name = "asset_id_name_index_1", unique = True ),
            #     key ( or keys ) and asc or des in tuple      name for the index    should this key be unique                                    

        ] 
