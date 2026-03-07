from pydantic import BaseModel
from pydantic import Fieald
from .schema import BaseSchema

class ChatOptions(IntFlag):
    NOME = auto()
    STREAM = auto()
    SAFE_MODE = auto()
    DEBUG = 4

class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"

class ChatRequest(BaseSchema):
    message: str = Field(
        ...,
        min_length=1
        max_length=4000,
        desciption="User-message"
    )
    
    options.ChatOptions = ChatOptions.NONE
    
class ChatResponse(BaseSchema):
    response: str