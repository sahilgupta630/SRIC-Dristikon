# SRIC Dristikon

## Overview

SRIC Dristikon is a comprehensive dashboard application developed for the Sponsored Research and Industrial Consultancy (SRIC) at IIT Kharagpur. The platform is designed to provide analytics, project management capabilities, and an AI-powered conversational interface for querying institutional data.

The project utilizes a modern tech stack with a React/TypeScript frontend for the dashboard and a Python backend (FastAPI/Streamlit) that handles data processing, RAG (Retrieval-Augmented Generation) based chat functionality, and database interactions.

## Key Features

- **Interactive Dashboard:** built with React and Radix UI components for a modern, responsive user experience.
- **AI-Powered Chat:** Includes a RAG-based chatbot (powered by Google Gemini and FAISS) to answer queries about projects, purchase guides, and GFR rules.
- **Vector Search:** Uses FAISS for efficient similarity search across document embeddings.
- **Data Visualization:** Integrated charts and metrics for dashboard analytics.
- **Backend API:** FastAPI services for handling requests and bridging the frontend with the AI engine.
- **Streamlit Interface:** An alternative/admin web interface for direct interaction with the chat system.

## Tech Stack

### Frontend
- **Framework:** React 18
- **Language:** TypeScript
- **Build Tool:** Vite
- **Styling:** Tailwind CSS, Radix UI Primitives, Lucide Icons
- **State/Animations:** Framer Motion

### Backend
- **Framework:** FastAPI / Streamlit
- **Language:** Python 3.x
- **AI/ML:** LangChain, Google Gemini Pro, FAISS (Vector DB)
- **Database:** SQLite
- **PDF Processing:** PyPDF

## Setup & Installation

### Prerequisites
- Node.js & npm
- Python 3.10+
- Google API Key (for Gemini)

### Frontend Setup
1. Navigate to the project root:
   ```bash
   cd sric_dsshboard
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended).
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Setup Environment Variables:
   - Create a `.env` file in the `backend/` directory.
   - Add your API Key: `GEMINI_API_KEY=your_key_here`

5. Initialize the Vector Database (if needed):
   ```bash
   python scripts/index.py
   # or the appropriate seed script provided in the backend folder
   ```

6. Run the Chat Interface (Streamlit):
   ```bash
   streamlit run ui_chat.py
   ```
   Or run the API server (FastAPI):
   ```bash
   uvicorn api:app --reload
   ```

## Workflow

1. **Document Ingestion:** PDFs and data files in `backend/data` are processed and indexed into a FAISS vector store.
2. **Query Processing:** User queries are matched against the indexed data using vector similarity.
3. **Response Generation:** Relevant context is retrieved and sent to the Gemini model to generate accurate, context-aware responses.
4. **Dashboard Visualization:** The React frontend consumes APIs to display project stats and chat interactions.
