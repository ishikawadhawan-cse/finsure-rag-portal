import os

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from rag.ingestion import ingest_pdf
from rag.retrieval import retrieve_relevant_chunks
from rag.llm import generate_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "data"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Banking RAG Chatbot Running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    chunks = ingest_pdf(file_path)

    return {
        "message": "PDF uploaded successfully",
        "chunks_created": chunks
    }


@app.post("/chat")
async def chat(query: str):

    relevant_chunks = retrieve_relevant_chunks(query)

    context = "\n".join(relevant_chunks)

    response = generate_response(query, context)

    return {
        "query": query,
        "response": response
    }
