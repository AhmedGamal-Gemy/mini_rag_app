from .BaseDataModel import BaseDataModel
from .db_schemes.asset import Asset
from models.enums.DatabaseEnums import DatabaseEnum
from models.enums.AssetTypesEnums import AssetTypeEnum
from bson.objectid import ObjectId
from pymongo import InsertOne


class AssetDataModel(BaseDataModel):

    def __init__(self, db_client : object):
        super().__init__(db_client=db_client)
        self.collection = db_client[DatabaseEnum.COLLECTION_ASSET_NAME.value]

    async def create_asset(self, asset : Asset ):
        
        result = await self.collection.insert_one( asset.model_dump( by_alias= True, exclude_unset=True ) )
        asset.id = result.inserted_id

        return asset
    
    async def get_asset(self, asset_id : str):

        asset = await self.collection.find_one({
            "_id" : ObjectId( asset_id )
        })

        return Asset(**asset)
    
    async def get_all_assets_by_project_id_type(self, asset_project_id : ObjectId, asset_type: AssetTypeEnum):
        
        assets = await self.collection.find({
            "asset_project_id" : str(asset_project_id),
            "asset_type" : asset_type.value,
        }).to_list(length = None)

        print("Querying with:", {
            "asset_project_id": str(asset_project_id),
            "asset_type": asset_type.value,
        })

        return [ Asset(**d) for d in assets ]
  
    async def create_many_assets(self, assets : list[Asset] ):

        operations = []

        for asset in assets:
            operation = InsertOne( asset.model_dump(by_alias= True, exclude_unset= True) )
            operations.append(operation)
        
        result = await self.collection.bulk_write( operations )

        return result.inserted_count
    
    async def delete_all_assets_by_project_id(self, project_id : ObjectId):
        
        result = await self.collection.delete_many({
            "asset_project_id" : project_id
        })

        return result.deleted_count
