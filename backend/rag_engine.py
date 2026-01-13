
import os
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RAGEngine:
    def __init__(self):
        load_dotenv()
        self.base_path = Path(__file__).parent
        self.faiss_db_path = self.base_path / "faiss_db"
        self.retrieval_k = 15
        self.retriever = None
        self.model = None
        self.system_instruction = """You are an expert procurement and finance assistant. Your task is to provide accurate and step-by-step guidance ONLY from the provided 'SRIC Purchase, Frameworks, and GFR Documents' context.

Your response must be clear and directly address the user's specific scenario.

CRITICAL INSTRUCTION FOR LINKS:
If the context contains any URLs or web links (e.g., sticking to https://sric.iitkgp.ac.in...), you MUST include them in your answer. Do not just mention the form name, provide the clickable link.
IMPORTANT: Remove any trailing numbers or query parameters (e.g., '?1763615476') from the links. The link should end with the file extension (like .pdf or .docx).

Instructions:
- Provide the answer directly without unnecessary pleasantries.
- Do NOT add a closing sentence like "Please ensure..." or "Hope this helps". A standard closing will be added automatically.

If the information is not in the context, you must state: 'I cannot find the specific procedure in the documents, please consult the SRIC department.' Do not invent information."""

    def initialize(self) -> bool:
        """Initialize the RAG system components."""
        try:
            if not self.faiss_db_path.exists():
                logger.error("Vector database not found! Please run the indexing script first.")
                raise FileNotFoundError("Vector database not found! Please run the indexing script first.")
            
            gemini_api_key = os.getenv("GEMINI_API_KEY")
            if not gemini_api_key:
                logger.error("GEMINI_API_KEY not found")
                raise ValueError("GEMINI_API_KEY not found in environment variables (required for embeddings)")
            
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                logger.error("GROQ_API_KEY not found")
                raise ValueError("GROQ_API_KEY not found in environment variables (required for generation)")
            
            logger.info("✅ API Keys loaded.")
            
            # Initialize embeddings
            embeddings = GoogleGenerativeAIEmbeddings(
                model="models/text-embedding-004",
                google_api_key=gemini_api_key
            )
            
            # Load vector store
            vectorstore = FAISS.load_local(
                str(self.faiss_db_path),
                embeddings,
                allow_dangerous_deserialization=True
            )
            
            self.retriever = vectorstore.as_retriever(
                search_kwargs={"k": self.retrieval_k}
            )
            
            # Initialize Groq Model
            self.model = ChatGroq(
                groq_api_key=groq_api_key,
                model_name='llama-3.3-70b-versatile',
                temperature=0.1,
                max_tokens=4096
            )
            logger.info("✅ RAG Engine initialized successfully.")
            return True
        except Exception as e:
            logger.error(f"Error initializing RAG system: {e}")
            return False

    def query(self, user_query: str, conversation_history: Optional[List[Dict[str, str]]] = None) -> Dict[str, Any]:
        """Process a user query."""
        if not self.model or not self.retriever:
             if not self.initialize():
                 return {"answer": "System not initialized and failed to start.", "sources": []}

        try:
            docs = self.retriever.invoke(user_query)
            
            # Create context with source information
            context_parts = []
            for doc in docs:
                source_name = Path(doc.metadata.get("source", "Unknown")).name
                context_parts.append(f"--- Source: {source_name} ---\n{doc.page_content}")
            
            context = "\n\n".join(context_parts)
            
            history_text = ""
            if conversation_history:
                recent_history = conversation_history[-6:]
                history_text = "\n\nPrevious Conversation:\n"
                for msg in recent_history:
                    role = "User" if msg.get("role") == "user" else "Assistant"
                    history_text += f"{role}: {msg.get('content')}\n"
                history_text += "\n"
            
            prompt = f"""{self.system_instruction}

Context from Purchase Documents:
{context}
{history_text}
Current Question: {user_query}

Instructions:
- If the current question is a follow-up or continuation of the previous conversation, use the conversation history to provide a contextual answer.
- If the current question is a new independent topic, answer it based solely on the context provided.
- Always base your answer on the Purchase Document context provided above.

Answer:"""
            
            response = self.model.invoke(prompt)
            
            # Check for negative response
            response_text = response.content
            response_lower = response_text.lower()
            is_negative = (
                "cannot find" in response_lower or 
                "can't find" in response_lower or
                "not found" in response_lower or
                "consult the sric department" in response_lower
            )
            
            if not is_negative:
                response_text += "\n\nIt is recommended to review the relevant sections of the Original Document for more detailed information. Please verify the answer with Original Document."
            
            sources = []
            if not is_negative:
                for doc in docs:
                    source_info = {
                        "content": doc.page_content,
                        "metadata": doc.metadata
                    }
                    sources.append(source_info)
            
            return {
                "answer": response_text,
                "sources": sources
            }
            
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return {"answer": f"Error processing query: {str(e)}", "sources": []}
