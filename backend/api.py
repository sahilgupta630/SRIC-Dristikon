
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Any, Dict
from rag_engine import RAGEngine

app = FastAPI(
    title="SRIC Dristikon Chatbot API",
    description="Backend API for the SRIC Dashboard Chatbot using RAG.",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG Engine
# In a production app, use a lifespan context manager, but global init is fine for this scale.
rag_engine = RAGEngine()
rag_engine.initialize()

class Message(BaseModel):
    role: str
    content: str
    
class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = []

class Source(BaseModel):
    content: str
    metadata: Dict[str, Any]

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]

@app.get("/", tags=["Health"], summary="Check API Status")
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok", "message": "SRIC Dristikon Chatbot API is operational"}

@app.post("/chat", response_model=ChatResponse, tags=["Chat"], summary="Query the RAG Chatbot")
def chat_endpoint(request: ChatRequest):
    """
    Send a message to the chatbot and get a response based on SRIC documents.
    """
    try:
        # Convert Pydantic models to dicts for the engine
        history_dicts = [msg.model_dump() for msg in request.history] if hasattr(Message, 'model_dump') else [msg.dict() for msg in request.history]
        
        result = rag_engine.query(request.message, history_dicts)
        
        # Check if the engine returned an error message in the answer
        if "Error processing query" in result.get("answer", ""):
            # We log it but still return the friendly error message to the user
            pass
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
