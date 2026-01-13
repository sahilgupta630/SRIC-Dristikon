# SRIC Dristikon

<div align="center">

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

</div>

---

## 🚀 Overview

**SRIC Dristikon** is a state-of-the-art comprehensive dashboard developed for the **Sponsored Research and Industrial Consultancy (SRIC)** at IIT Kharagpur. The platform is engineered to empower administrators with advanced analytics, seamless project management, and an intelligent AI-driven query system.

Bridging the gap between complex institutional data and actionable insights, SRIC Dristikon utilizes a high-performance **React/TypeScript** frontend and a robust **Python (FastAPI/Streamlit)** backend to deliver a premium user experience.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 📊 **Interactive Dashboard** | Built with **React** & **Radix UI** for specialized, responsive data visualization and management. |
| 🤖 **AI-Powered Chat** | A RAG-based assistant powered by **Gemini Pro** & **LangChain** to answer queries on purchase guides, rules, and projects. |
| 🔍 **Vector Search** | High-speed semantic search using **FAISS** to instantly retrieve relevant document contexts. |
| 📈 **Deep Analytics** | Integrated charts and real-time metrics to track project statuses and funding. |
| ⚡ **FastAPI Backend** | A high-performance asynchronous API layer bridging the UI with the AI engine. |
| 🖥️ **Admin Interface** | A dedicated **Streamlit** interface for direct interaction with the chat system and database management. |

---

## 🛠️ Tech Stack

### 🎨 Frontend
- **Framework:** ⚛️ React 18
- **Language:** 📘 TypeScript
- **Build Tool:** ⚡ Vite
- **Styling:** 🌬️ Tailwind CSS, Radix UI Primitives
- **Icons:** 🧩 Lucide React
- **Animation:** 🎬 Framer Motion

### 🐍 Backend
- **Framework:** 🚀 FastAPI / 👑 Streamlit
- **Language:** 🐍 Python 3.10+
- **AI/ML:** 🧠 LangChain, Google Gemini Pro
- **Vector DB:** 💾 FAISS
- **Database:** 🗄️ SQLite
- **Processing:** 📄 PyPDF

---

## ⚙️ Setup & Installation

Follow these steps to get the project running on your local machine.

### 📋 Prerequisites
- **Node.js** (v18+) & **npm**
- **Python** (v3.10+)
- **Google API Key** (for Gemini AI)

### 🖥️ Frontend Setup
1.  **Navigate to the project root:**
    ```bash
    cd sric_dsshboard
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Run the development server:**
    ```bash
    npm run dev
    ```
    > The dashboard will be available at `http://localhost:5173`

### 🔌 Backend Setup
1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment:**
    Create a `.env` file in the `backend/` directory:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```
4.  **Initialize Knowledge Base:**
    ```bash
    python scripts/index.py
    ```
5.  **Run the Server:**
    - Modified for API interactions:
      ```bash
      uvicorn api:app --reload
      ```
    - Or for the Streamlit Interface:
      ```bash
      streamlit run ui_chat.py
      ```

---

## 🔄 Workflow Architecture

1.  **📥 Document Ingestion**: PDFs (Rules, Guidelines) are parsed and chunked.
2.  **🧠 Embedding**: Text chunks are converted to vectors and stored in **FAISS**.
3.  **💬 Users Query**: Front-end sends natural language questions to the Backend.
4.  **🔍 Retrieval**: System finds the most relevant context from the vector store.
5.  **📝 Generation**: **Gemini Pro** generates an accurate answer based on the retrieved context.
6.  **📊 Visualization**: The React Dashboard displays the answer along with relevant project stats.

---


