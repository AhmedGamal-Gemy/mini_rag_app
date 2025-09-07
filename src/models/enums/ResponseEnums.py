from enum import Enum

class ResponseSignal(Enum):

    FILE_TYPE_NOT_SUPPORTED = "file type is not supported"
    FILE_SIZE_EXCEEDED = "file size is bigger than the max"
    FILE_UPLOAD_SUCCESS = "file upload success"
    FILE_UPLOAD_FAILED = "file upload failed"
    PROCESSING_FAILED = "process failed"