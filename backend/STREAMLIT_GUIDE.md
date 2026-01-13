# Streamlit UI Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install streamlit>=1.28.0
```

Or install all requirements:
```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App
```bash
streamlit run ui_chat.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

## Features

### 🎨 User Interface
- **Responsive Chat Interface**: Clean, modern chat UI with message history
- **Source Document Display**: Toggle to view retrieved document chunks
- **Session Management**: Persistent chat history during your session
- **Clear Chat**: Reset conversation with one click

### ⚙️ Settings (Sidebar)
- **Show/Hide Sources**: Toggle display of retrieved document chunks
- **Statistics**: View message count and retrieval settings
- **System Status**: Check vector database and API key status

### 💬 Chat Features
- **Real-time Responses**: Powered by Gemini 2.5 Flash
- **Context-Aware**: Uses top 5 most relevant document chunks
- **Source Citations**: See exactly which documents were used
- **Error Handling**: Graceful error messages and recovery

## Configuration

The application uses the same configuration as the CLI version:
- **Vector Database**: `faiss_db/` directory
- **API Key**: Set in `.env` file as `GEMINI_API_KEY`
- **Retrieval Count**: 5 chunks (configurable in code)

## Troubleshooting

### Vector Database Not Found
```
❌ Vector database not found!
```
**Solution**: Run the indexing script first:
```bash
python scripts/index.py
```

### API Key Missing
```
❌ GEMINI_API_KEY not found
```
**Solution**: Create/update `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

### Port Already in Use
If port 8501 is busy, specify a different port:
```bash
streamlit run ui_chat.py --server.port 8502
```

## Advanced Configuration

### Custom Streamlit Settings
Create `.streamlit/config.toml` in your project root:

```toml
[server]
port = 8501
headless = true

[theme]
primaryColor = "#2196F3"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F5F5"
textColor = "#262730"
font = "sans serif"
```

### Deployment Options

#### Local Network Access
```bash
streamlit run ui_chat.py --server.address 0.0.0.0
```

#### Production Deployment
For production, consider:
- **Streamlit Cloud**: Free hosting for public apps
- **Docker**: Containerize the application
- **Cloud Platforms**: Deploy to AWS, GCP, Azure

## Comparison: CLI vs Web UI

| Feature | CLI (`cli_chat.py`) | Web UI (`ui_chat.py`) |
|---------|---------------------|----------------------|
| Interface | Terminal | Web Browser |
| Chat History | Session only | Persistent in session |
| Source Display | Not available | Toggle on/off |
| Multi-user | No | Yes (separate sessions) |
| Accessibility | Command line | Any device with browser |
| Best For | Quick queries, automation | Interactive exploration |

## Usage Tips

1. **First Time Setup**: Always run the indexing script before using either interface
2. **Source Documents**: Enable "Show source documents" to understand where answers come from
3. **Clear Chat**: Use the clear button to start fresh conversations
4. **Session State**: Your chat history persists until you close the browser tab or clear it

## File Structure
```
PDF_CHATBOT/
├── ui_chat.py              # Streamlit web interface (NEW)
├── cli_chat.py             # Command-line interface
├── scripts/
│   └── index.py            # Document indexing script
├── faiss_db/               # Vector database (created after indexing)
├── data/                   # PDF documents
├── requirements.txt        # Python dependencies
└── .env                    # API keys and configuration
```
