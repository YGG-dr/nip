from pydantic import BaseModel
from pydantic import Field
from .schema import BaseSchema
from enum import IntFlag, Enum, auto

class ChatOptions(IntFlag):
    NONE = 0
    STREAM = auto()
    SAFE_MODE = auto()
    DEBUG = auto()

class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"

class ChatRequest(BaseSchema):
    message: str = Field(..., min_length=1, max_length=4000, desciption="User-message" )
    options: ChatOptions = ChatOptions.NONE
    
class ChatResponse(BaseSchema):
    response: str