import chromadb
from rag.ingestion import collection
from rag.embeddings import embedding_model


# Load ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_collection(name="banking_docs")


def retrieve_relevant_chunks(query, top_k=3):

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]

    return documents
