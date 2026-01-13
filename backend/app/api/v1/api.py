
from fastapi import APIRouter
from app.api.v1.endpoints import dashboard, chatbot

api_router = APIRouter()
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(chatbot.router, prefix="/chat", tags=["chat"])
