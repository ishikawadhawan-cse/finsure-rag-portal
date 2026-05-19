import os
import uuid
import chromadb

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.embeddings import embedding_model


# ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(
    name="banking_docs"
)


def extract_text_from_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    return chunks


def store_embeddings(chunks):

    existing_count = collection.count()

    for i, chunk in enumerate(chunks):

        embedding = embedding_model.encode(chunk).tolist()

        collection.add(
            ids=[str(existing_count + i)],
            embeddings=[embedding],
            documents=[chunk]
        )

def ingest_pdf(pdf_path):

    text = extract_text_from_pdf(pdf_path)

    chunks = chunk_text(text)

    store_embeddings(chunks)

    return len(chunks)
