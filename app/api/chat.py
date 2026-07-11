from fastapi import APIRouter
from app.services.chat_service import chat_stream
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str
# v1.0 普通輸出
# @router.post("/chat")
# def chat_api(request: ChatRequest):
#     response = chat(request.message)
#     return {"response": response}

@router.post("/chat")
def chat_api(request: ChatRequest):
    response = chat_stream(request.session_id, request.message)
    def generate():
        for chunk in response:
            yield chunk
    return StreamingResponse(generate(), media_type="text/event-stream")