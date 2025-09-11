from enum import Enum

class AssetTypeEnum(str,Enum):
    
    FILE = "file"
    URL = "url"
    DATABASE_CONNECTION = "db_connection"

