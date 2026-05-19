FinSure – Financial Intelligence RAG Portal
FinSure is an enterprise-grade Retrieval-Augmented Generation (RAG) platform designed for secure financial document analysis and intelligent information retrieval.
The system allows users to upload banking and financial PDFs, perform semantic search, and generate AI-powered responses using advanced language models and vector embeddings.


Features
- Secure PDF Upload System
- AI-Powered Financial Question Answering
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database Integration
- Semantic Search using Sentence Transformers
- FastAPI Backend
- Streamlit Enterprise UI
- Real-Time Financial Insight Generation
- Modern Banking-Inspired User Interface


Tech Stack
Frontend
- Streamlit

Backend
- FastAPI
- Uvicorn

AI & RAG
- OpenAI / OpenRouter API
- Sentence Transformers
- ChromaDB

Document Processing
- PyPDF
- LangChain Text Splitters


Project Structure

```bash

banking-rag-chatbot/

│

├── app.py

├── frontend.py

├── requirements.txt

├── README.md

│

├── rag/

│   ├── embeddings.py

│   ├── ingestion.py

│   ├── retrieval.py

│   └── llm.py

│

├── uploads/

├── chroma_db/

└── data/
