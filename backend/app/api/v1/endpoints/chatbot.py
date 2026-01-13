
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
import sys
import os

# Add backend root to sys.path to allow importing legacy modules
# Assuming app is run from backend/ directory
sys.path.append(os.getcwd())

try:
    from rag_engine import RAGEngine
except ImportError:
    # Fallback if run from different CWD
    sys.path.append(os.path.join(os.getcwd(), ".."))
    from rag_engine import RAGEngine

router = APIRouter()

# Initialize RAG Engine (Singleton-ish)
rag_engine = RAGEngine()
# Try initialize, catch error if dependencies missing during refactor
try:
    rag_engine.initialize()
except Exception as e:
    print(f"Warning: RAG Engine failed to initialize: {e}")

class Message(BaseModel):
    role: str
    content: str
    
class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = []

class Source(BaseModel):
    content: str
    metadata: dict

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]

@router.post("/", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    result = rag_engine.query(request.message, [msg.dict() for msg in request.history])
    return result
