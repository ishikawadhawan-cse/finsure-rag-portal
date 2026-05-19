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




INSTALLATION
Clone Repository
git clone https://github.com/your-username/finsure-rag-portal.git
cd finsure-rag-portal

CREATE VIRTUAL ENVIRONMENT
python -m venv venv
source venv/bin/activate

INSTALL DEPENDENCIES
pip install -r requirements.txt

RUN BACKEND
python -m uvicorn app:app --reload

RUN FRONTEND
streamlit run frontend.py

WORKFLOW
1. Upload Financial PDF Documents
2. Documents are chunked and embedded
3. Embeddings are stored in ChromaDB
4. User asks financial questions
5. Relevant chunks are retrieved
6. AI generates contextual responses

FUTURE ENHANCEMENTS
* Multi-document querying
* Financial dashboard analytics
* OCR support
* Chat history persistence
* User authentication
* Cloud deployment
* Role-based access control

AUTHOR

Ishika Wadhawan

B.Tech CSE – AI & ML
UPES Dehradun

LinkedIn:
https://linkedin.com/in/ishika-wadhawan


LICENSE
This project is developed for educational and research purposes.
