from openai import OpenAI

from app.core.config import get_settings
from app.models.chat_models import ChatOptions, Role

class ChatService:
    def __init__(self) -> None:
        self.sttings = get_settings()
        self.client: OpenAI = OpenAI()
        
    def ask(self, message: str, options: ChatOptions = ChatOptions.NONE) -> str:
        if options & ChatOptions.DEBUG:
            print(f"[DEBUG] Incoming message: {message}")
        
        response = self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    "role": Role.USER.value,
                    "content": message
                }
            ]
        )
        
        answer: str | None = response.choices[0].message.content
        
        if answer is None:
            return ""
        
        if options & ChatOptions.SAFE_MODE:
            answer = answer.strip()
            
        return answer
        