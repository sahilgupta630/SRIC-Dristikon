"""
Streamlit Web UI for PurchaseDoc-RAG
This script provides an interactive web-based chat interface for querying
the purchase guide using RAG (Retrieval-Augmented Generation).
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

# Configure UTF-8 encoding for Windows
if sys.platform == 'win32':
    import io
    try:
        if hasattr(sys.stdout, 'buffer') and not isinstance(sys.stdout, io.TextIOWrapper):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        if hasattr(sys.stderr, 'buffer') and not isinstance(sys.stderr, io.TextIOWrapper):
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except (AttributeError, ValueError):
        pass

# Load environment variables
load_dotenv()

# ============================================================================
# A. CONFIGURATION
# ============================================================================

# Constants
FAISS_DB_PATH = Path(__file__).parent / "faiss_db"
RETRIEVAL_K = 10 

LOGO_URL = "https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/IIT_Kharagpur_Logo.svg/800px-IIT_Kharagpur_Logo.svg.png"


# Page configuration
st.set_page_config(
    page_title="SRIC Compass | IIT Kharagpur",
    page_icon=LOGO_URL,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern dashboard look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Global Clean Look */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Remove hardcoded background colors to respect Light/Dark mode */
    .stApp {
        /* background-color: #f8fafc;  <-- REMOVED to allow theme inheritance */
    }
    
    /* Sidebar styling - Transparent/Inherit to respect theme */
    [data-testid="stSidebar"] {
        /* background-color: #ffffff; <-- REMOVED */
        border-right: 1px solid var(--text-color-20); /* Uses Streamlit variable */
    }
    
    /* Main container styling */
    .main {
        max-width: 900px;
        margin: 0 auto;
    }

    /* Greeting Header - Adaptable color */
    .greeting-header {
        text-align: center;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
        font-size: 2rem;
        font-weight: 600;
        color: var(--text-color); /* Streamlit variable */
    }
    .greeting-subtext {
        text-align: center;
        color: var(--text-color-80); /* 80% opacity text */
        margin-bottom: 3rem;
        font-size: 1.1rem;
    }
    
    /* --------------------------------------------------------
       BUTTON STYLING (Topic Cards)
       -------------------------------------------------------- */
    
    div.stButton > button {
        border-radius: 8px;
        transition: all 0.2s ease;
    }

    /* SIDEBAR Buttons */
    /* Target the button element more specifically within the sidebar */
    [data-testid="stSidebar"] div.stButton button {
        background-color: var(--secondary-background-color) !important;
        border: 1px solid #cbd5e1 !important; /* Fixed: Use standard gray instead of invalid var */
        color: var(--text-color) !important;
        font-weight: 600;
        padding: 0.5rem 1rem;
        width: 100%;
        border-radius: 8px !important; /* Ensure rounded corners */
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Add slight shadow for 'box' feel */
    }
    [data-testid="stSidebar"] div.stButton button:hover {
        border-color: var(--primary-color) !important;
        color: var(--primary-color) !important;
        background-color: var(--background-color) !important;
    }

    /* MAIN AREA Buttons */
    .main div.stButton > button {
        background-color: var(--secondary-background-color);
        border: 1px solid #cbd5e1; /* Fixed: Use standard gray */
        border-radius: 12px;
        padding: 1.5rem;
        text-align: left;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        height: 100%;
        min-height: 140px; 
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        color: var(--text-color); 
    }
    .main div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
        border-color: var(--primary-color);
    }
    .main div.stButton > button p {
        font-size: 1rem !important;
        line-height: 1.5 !important;
        color: var(--text-color);
    }
    .main div.stButton > button p:first-child {
        font-weight: 700;
        margin-bottom: 0.25rem;
        color: var(--text-color) !important;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background-color: transparent;
        padding: 1.5rem 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }
    .stChatMessage[data-testid="user-message"] {
        background-color: var(--secondary-background-color); /* Adaptive User BG */
        border: 1px solid var(--text-color-20);
    }
    .stChatMessage[data-testid="assistant-message"] {
        background-color: transparent; /* Cleaner look for assistant */
        border: 1px solid var(--text-color-20);
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* Chat Input styling */
    .stChatInputContainer {
        padding-bottom: 2rem;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* header {visibility: hidden;}  <-- RESTORED header to show sidebar toggle */
    
    /* Hide anchor links (chain icons) next to headers */
    .st-emotion-cache-1629p8f h1 a, 
    .st-emotion-cache-1629p8f h2 a, 
    .st-emotion-cache-1629p8f h3 a {
        display: none !important;
    }
    a.anchor-link {
        display: none !important;
    }
    
    /* LOGO VISIBILITY FIX FOR DARK MODE 
       This adds a shadow matching the text color. 
       - In Dark Mode: Text is white -> Logo gets white glow (visible).
       - In Light Mode: Text is dark -> Logo gets dark glow (subtle/natural).
    */
    img[src*="IIT_Kharagpur_Logo"] {
        filter: drop-shadow(0 0 0.75px var(--text-color));
    }
    
</style>



""", unsafe_allow_html=True)


# ============================================================================
# B. RAG ENGINE
# ============================================================================

@st.cache_resource
def initialize_rag_system():
    try:
        if not FAISS_DB_PATH.exists():
            st.error("❌ Vector database not found! Please run the indexing script first.")
            return None, None, None
        
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            st.error("❌ GEMINI_API_KEY not found (required for embeddings)")
            return None, None, None
            
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            st.error("❌ GROQ_API_KEY not found (required for generation)")
            return None, None, None
        
        embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        
        vectorstore = FAISS.load_local(
            str(FAISS_DB_PATH),
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        retriever = vectorstore.as_retriever(search_kwargs={"k": RETRIEVAL_K})
    
        model = ChatGroq(
            groq_api_key=groq_api_key,
            model_name='llama-3.3-70b-versatile',
            temperature=0.1,
            max_tokens=4096
        )
    
        system_instruction = """You are an expert procurement and finance assistant. Your task is to provide accurate and step-by-step guidance ONLY from the provided 'SRIC Purchase, Frameworks, and GFR Documents' context.

### RESPONSE FORMATTING INSTRUCTIONS (CRITICAL):
- **Structure**: Use a clean, structured format. Avoid long, dense blocks of text.
- **Bullet Points**: ALWAYS use bullet points or numbered lists for steps, rules, or lists of items.
- **Markdown**: Use **bold** text to highlight key terms, thresholds (e.g., **Rs. 2.5 Lakhs**), and important actions.
- **Clarity**: Keep paragraphs short and concise.

### LINK INSTRUCTIONS:
- If URLs are present in the context, format them as code snippets: `example.com`

### ANSWERING RULES:
- Provide the answer directly without propertied pleasantries.
- Do NOT add a closing sentence like "Hope this helps".
- If the information is not in the context, state: 'I cannot find the specific procedure in the document, please consult the SRIC department.'"""
        
        return retriever, model, system_instruction
    
    except Exception as e:

        st.error(f"❌ Error initializing RAG system: {str(e)}")
        return None, None, None


def get_rag_response(user_query, retriever, model, system_instruction, conversation_history=None):
    try:
        docs = retriever.invoke(user_query)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        history_text = ""
        if conversation_history and len(conversation_history) > 0:
            recent_history = conversation_history[-6:]
            history_text = "\n\nPrevious Conversation:\n"
            for msg in recent_history:
                role = "User" if msg["role"] == "user" else "Assistant"
                history_text += f"{role}: {msg['content']}\n"
            history_text += "\n"
        
        prompt = f"""{system_instruction}

Context from Purchase Document:
{context}
{history_text}
Current Question: {user_query}

Instructions:
- If the current question is a follow-up or continuation of the previous conversation, use the conversation history to provide a contextual answer.
- If the current question is a new independent topic, answer it based solely on the context provided.
- Always base your answer on the Purchase Document context provided above.

Answer:"""
        
        response = model.invoke(prompt)
        response_text = response.content
        response_lower = response_text.lower()
        is_negative = (
            "cannot find" in response_lower or 
            "can't find" in response_lower or
            "not found" in response_lower or
            "consult the sric department" in response_lower
        )

        if not is_negative:
             response_text += "\n\nIt is recommended to review the relevant sections of the Original Document for more detailed information. Please verify the answer with original documents."
        
        show_sources = not is_negative
        return response_text, docs, show_sources
    
    except Exception as e:
        st.error(f"❌ Error processing query: {str(e)}")
        return None, None, False


# ============================================================================
# C. MAIN APPLICATION
# ============================================================================

def main():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "show_sources" not in st.session_state:
        st.session_state.show_sources = True

    retriever, model, system_instruction = initialize_rag_system()
    if not retriever or not model:
        st.stop()
    
    # ------------------------------------------------------------------------
    # SIDEBAR
    # ------------------------------------------------------------------------
    with st.sidebar:
        # Logo and Title
        st.image(LOGO_URL, width=80)
        st.markdown("<h2 style='margin-top:0;'>SRIC Compass</h2>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 0.9rem; color: #64748b; margin-bottom: 2rem;'>IIT Kharagpur</div>", unsafe_allow_html=True)
        
        if st.button("➕ New Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("---")
        st.markdown("### Settings")
        st.session_state.show_sources = st.checkbox("Show Sources", value=st.session_state.show_sources)
    
    # ------------------------------------------------------------------------
    # MAIN CONTENT
    # ------------------------------------------------------------------------
    hour = datetime.now().hour
    if 5 <= hour < 12: greeting = "Good morning"
    elif 12 <= hour < 18: greeting = "Good afternoon"
    else: greeting = "Good evening"

    # EMPTY CHAT STATE (Landing Page)
    if len(st.session_state.messages) == 0:
        # Centered Layout
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"<div style='text-align: center;'><img src='{LOGO_URL}' width='100'></div>", unsafe_allow_html=True)
            st.markdown(f"<h1 class='greeting-header'>{greeting}</h1>", unsafe_allow_html=True)
            st.markdown("<div class='greeting-subtext'>How can I assist you with SRIC procedures today?</div>", unsafe_allow_html=True)
        
        # Topic Cards
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("📝 Purchase Guide\n\nProcurement guidelines", use_container_width=True):
                 st.session_state.messages.append({"role": "user", "content": "What are the general guidelines for purchase?", "timestamp": datetime.now()})
                 st.rerun()
        with c2:
            if st.button("⚖️ GFR Rules\n\nGeneral Financial Rules 2017", use_container_width=True):
                 st.session_state.messages.append({"role": "user", "content": "Explain the key GFR rules for project purchases.", "timestamp": datetime.now()})
                 st.rerun()
        with c3:
            if st.button("🏗️ Frameworks\n\nSRIC Project Management", use_container_width=True):
                 st.session_state.messages.append({"role": "user", "content": "What are the SRIC project frameworks?", "timestamp": datetime.now()})
                 st.rerun()

    # ACTIVE CHAT STATE
    else:
        # Chat Header
        c1, c2 = st.columns([0.1, 0.9])
        with c1:
            st.image(LOGO_URL, width=40)
        with c2:
            st.markdown("<h3 style='margin: 0; padding-top: 5px;'>SRIC Compass</h3>", unsafe_allow_html=True)
        st.markdown("---")
        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if (message["role"] == "assistant" and 
                    st.session_state.show_sources and 
                    message.get("sources")):
                    
                    # Deduplication
                    unique_sources = []
                    seen_sources = set()
                    for doc in message["sources"]:
                        # Robust filename extraction (handles Windows paths on Linux servers)
                        source_path = doc.metadata.get("source", "Unknown")
                        name = source_path.replace("\\", "/").split("/")[-1]
                        page = doc.metadata.get("page", "Unknown")
                        key = (name, page)
                        if key not in seen_sources:
                            seen_sources.add(key)
                            unique_sources.append(key)
                    
                    # Sort sources
                    unique_sources.sort(key=lambda x: (x[0], int(x[1]) if str(x[1]).isdigit() else 99999))

                    with st.expander("📄 View References (Page Numbers)"):
                        st.markdown("References from Original Document:")
                        for name, page in unique_sources:
                            st.markdown(f"**{name}** — Page: {page}")

    # CHAT INPUT
    if user_input := st.chat_input("Ask about detailed procedures, GFR rules, or frameworks..."):
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now()
        })
        st.rerun()

    # PROCESS RESPONSE
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with st.chat_message("assistant"):
            with st.spinner("Analyzing documents..."):
                try:
                    response, docs, show = get_rag_response(
                        st.session_state.messages[-1]["content"],
                        retriever, model, system_instruction,
                        st.session_state.messages[:-1]
                    )
                
                    if response:
                        st.markdown(response)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": response,
                            "sources": docs if show else None,
                            "timestamp": datetime.now()
                        })
                        if show and docs and st.session_state.show_sources:
                            unique = []
                            seen = set()
                            for d in docs:
                                # Robust filename extraction
                                src_path = d.metadata.get("source", "Unknown")
                                n = src_path.replace("\\", "/").split("/")[-1]
                                p = d.metadata.get("page", "Unknown")
                                k = (n, p)
                                if k not in seen:
                                    seen.add(k)
                                    unique.append(k)
                            
                            # Sort sources
                            unique.sort(key=lambda x: (x[0], int(x[1]) if str(x[1]).isdigit() else 99999))

                            with st.expander("📄 View References (Page Numbers)"):
                                st.markdown("References from Original Document:")
                                for n, p in unique:
                                    st.markdown(f"**{n}** — Page: {p}")
                    else:
                        st.error("Failed to respond.")
                        st.session_state.messages.pop()
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    st.session_state.messages.pop()

if __name__ == "__main__":
    main()
