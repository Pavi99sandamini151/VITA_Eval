from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.chatbot import chatbot_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        reply = chatbot_response(req.message)
        return {"reply": reply}
    except Exception as e:
        print(f"Error in /chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))
