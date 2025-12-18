from fastapi import FastAPI
from app.api.chat_routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Chatbot API is running"}
