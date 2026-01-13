"""
Indexing Script for BoughtyBOT V1
This script loads the purchase guide PDF, splits it into chunks, 
generates embeddings, and stores them in a Chroma vector database.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import pdfplumber
import pypdfium2 as pdfium
import pytesseract
from PIL import Image
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Set Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def load_pdf_with_ocr(file_path):
    """
    Hybrid loader: 
    1. Tries standard text extraction (pdfplumber)
    2. If text is low (<50 chars), renders page as image and runs OCR (tesseract)
    """
    documents = []
    print(f"     (Using OCR-enabled loader for {Path(file_path).name})")
    
    try:
        # Open with pdfplumber for text
        with pdfplumber.open(file_path) as pdf:
            # Open with pdfium for images (OCR fallback)
            pdf_renderer = pdfium.PdfDocument(file_path)
            
            for i, page in enumerate(pdf.pages):
                # Attempt 1: Standard Searchable Text
                text = page.extract_text() or ""
                
                # Attempt 2: OCR if text is missing/sparse (likely a scanned page)
                if len(text.strip()) < 50:
                    print(f"      - Page {i+1}: Text sparse ({len(text.strip())} chars). Running OCR...")
                    try:
                        # Render page to image (scale=3 for high quality)
                        renderer_page = pdf_renderer[i]
                        bitmap = renderer_page.render(scale=3)
                        pil_image = bitmap.to_pil()
                        
                        # Run OCR
                        ocr_text = pytesseract.image_to_string(pil_image)
                        
                        if len(ocr_text.strip()) > len(text.strip()):
                            text = ocr_text
                            print(f"        -> OCR recovered {len(text)} chars")
                    except Exception as ocr_err:
                        print(f"        -> OCR Failed: {ocr_err}")

                if text.strip():
                    documents.append(Document(
                        page_content=text,
                        metadata={"source": str(file_path), "page": i + 1}
                    ))
                    
    except Exception as e:
        print(f"   ⚠️ Error reading {file_path}: {e}")
        import traceback
        traceback.print_exc()
        
    return documents

# Configure UTF-8 encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Load environment variables
load_dotenv()

# Constants
PDF_PATH = Path(__file__).parent.parent / "data" / "purchase_guide.pdf"
FAISS_DB_PATH = Path(__file__).parent.parent / "faiss_db"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def create_index():
    """
    Create the vector database index from the purchase guide PDF.
    
    Steps:
    1. Load the PDF document
    2. Split text into chunks with overlap
    3. Generate embeddings using Google's text-embedding-004 model
    4. Store embeddings in Faiss vector database
    """
    
    # Check if data directory exists
    if not PDF_PATH.parent.exists():
        print(f"❌ Error: Data directory not found at {PDF_PATH.parent}")
        sys.exit(1)
    
    print(f"📂 Scanning for PDFs in: {PDF_PATH.parent}")
    
    # Check for API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in environment variables")
        print("Please create a .env file with your API key:")
        print("GEMINI_API_KEY=your_api_key_here")
        sys.exit(1)
    
    try:
        documents = []
        pdf_files = list(PDF_PATH.parent.glob("*.pdf"))
        
        if not pdf_files:
            print(f"❌ Error: No PDF files found in {PDF_PATH.parent}")
            sys.exit(1)

        print(f"Found {len(pdf_files)} PDF files to process.")

        for pdf_file in pdf_files:
            print(f"📄 Loading PDF: {pdf_file.name}")
            docs = load_pdf_with_ocr(str(pdf_file))
            print(f"   - Loaded {len(docs)} pages")
            documents.extend(docs)
            
        print(f"✅ Total loaded {len(documents)} pages from all PDFs")
        
        # Split documents into chunks
        print(f"📝 Splitting text into chunks (size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP})...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)
        print(f"✅ Created {len(chunks)} total text chunks")
        
        # Initialize embeddings
        print("🔄 Initializing Google Generative AI Embeddings (text-embedding-004)...")
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004"
        )
        
        # Create and persist vector store
        print(f"💾 Creating FAISS vector database at: {FAISS_DB_PATH}")
        
        # Remove existing database if it exists
        if FAISS_DB_PATH.exists():
            print("⚠️  Existing database found. Removing old index...")
            import shutil
            shutil.rmtree(FAISS_DB_PATH)
        
        # Create directory for FAISS database
        FAISS_DB_PATH.mkdir(parents=True, exist_ok=True)
        
        # Create new vector store
        vectorstore = FAISS.from_documents(
            documents=chunks,
            embedding=embeddings
        )
        
        # Save the vector store to disk
        vectorstore.save_local(str(FAISS_DB_PATH))
        
        print(f"✅ Successfully created vector database with {len(chunks)} chunks")
        print(f"📁 Database persisted to: {FAISS_DB_PATH}")
        print("\n🎉 Indexing complete! You can now run the chatbot with: python cli_chat.py")
        
    except Exception as e:
        print(f"❌ Error during indexing: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    print("=" * 60)
    print("PurchaseDoc-RAG-CLI - Indexing Script")
    print("=" * 60)
    create_index()
