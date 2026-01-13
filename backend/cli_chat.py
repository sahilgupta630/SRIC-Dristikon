"""
Interactive CLI Chat Interface for PurchaseDoc-RAG-CLI
This script provides an interactive command-line interface for querying
the purchase guide using RAG (Retrieval-Augmented Generation).
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

# Configure UTF-8 encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Load environment variables
load_dotenv()

# Constants
FAISS_DB_PATH = Path(__file__).parent / "faiss_db"
RETRIEVAL_K = 15  # Number of relevant chunks to retrieve (increased to capture more context)


def run_chat_cli():
    """
    Run the interactive chat CLI for querying the purchase guide.
    
    Features:
    - Loads persisted FAISS vector database
    - Uses Groq (Llama 3) for fast, accurate responses
    - Retrieves top 5 relevant document chunks
    - Enforces strict adherence to document content
    - Provides interactive loop for continuous queries
    """
    
    # Check if vector database exists
    if not FAISS_DB_PATH.exists():
        print("❌ Error: Vector database not found!")
        print("Please run the indexing script first:")
        print("  python scripts/index.py")
        sys.exit(1)
    
    # Check for API key
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        print("❌ Error: GEMINI_API_KEY not found in environment variables")
        sys.exit(1)
        
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        print("❌ Error: GROQ_API_KEY not found in environment variables")
        print("Please add GROQ_API_KEY=... to your .env file")
        sys.exit(1)
    
    try:
        print("🔄 Loading vector database...")
        
        # Initialize embeddings (must match the ones used during indexing)
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004"
        )
        
        # Load the persisted vector store
        vectorstore = FAISS.load_local(
            str(FAISS_DB_PATH),
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        # Create retriever
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": RETRIEVAL_K}
        )
        
        print("🤖 Initializing Groq (Llama 3) model...")
        
        # Initialize the model directly
        model = ChatGroq(
            groq_api_key=groq_api_key,
            model_name='llama-3.3-70b-versatile',
            temperature=0.1,
            max_tokens=2048
        )
        
        # Define the system instruction (optimized for speed)
        system_instruction = """You are a procurement assistant. Provide accurate guidance from the Purchase Documents context.

Critical Rules:
1. Read ALL context sections thoroughly
2. List EVERY document/requirement mentioned across all sections
3. Be complete and accurate
4. If info is missing: state 'Consult the SRIC department'
5. Never invent information"""
        
        print("✅ Chatbot ready!\n")
        print("=" * 60)
        print("PurchaseDoc-RAG-CLI - Interactive Chat")
        print("=" * 60)
        print("Ask questions about purchase procedures and policies.")
        print("Type 'exit' to quit.\n")
        
        # Interactive loop
        while True:
            try:
                # Get user input
                user_input = input("\n> Enter your question (or 'exit' to quit): ").strip()
                
                # Check for exit command
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("\n👋 Thank you for using PurchaseDoc-RAG-CLI. Goodbye!")
                    break
                
                # Skip empty inputs
                if not user_input:
                    continue
                
                # Process the query
                print("\n🔍 Searching document...")
                
                # Retrieve relevant documents
                docs = retriever.invoke(user_input)
                
                # Debug: Show number of chunks retrieved
                print(f"📊 Retrieved {len(docs)} relevant chunks from the database")
                
                # Format context from retrieved documents
                context_parts = []
                for doc in docs:
                    source_name = Path(doc.metadata.get("source", "Unknown")).name
                    context_parts.append(f"--- Source: {source_name} ---\n{doc.page_content}")
                context = "\n\n".join(context_parts)
                
                # Create the prompt
                prompt = f"""{system_instruction}

Context from Purchase Documents:
{context}

Question: {user_input}

Answer:"""
                
                # Generate response with streaming
                print("\n" + "=" * 60)
                print("📋 Answer:")
                print("=" * 60)
                
                response = model.stream(prompt)
                
                # Stream the response token by token
                full_response = ""
                try:
                    for chunk in response:
                        content = chunk.content
                        if content:
                            print(content, end='', flush=True)
                            full_response += content
                    
                    print("\n" + "=" * 60)
                    
                    # Check if we got any response
                    if not full_response.strip():
                        print("\n⚠️ Warning: Empty response received")
                        print("Please try rephrasing your question.")
                        print("=" * 60)
                        continue
                        
                except Exception as stream_error:
                    print(f"\n\n⚠️ Streaming error: {str(stream_error)}")
                    print("Trying non-streaming mode...")
                    
                    # Fallback to non-streaming if streaming fails
                    response = model.invoke(prompt)
                    print(response.content)
                    print("=" * 60)
                
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error processing query: {str(e)}")
                print("Please try again with a different question.")
    
    except Exception as e:
        print(f"❌ Error initializing chatbot: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_chat_cli()

