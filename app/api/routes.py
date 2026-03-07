from fastapi import APIRouter
from app.models.chat_models import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    answer = chat_service.ask(
        req.message,
        req.options
    )
    
    return ChatResponse(response=answer)