from langchain.vectorstores import Chroma
from utils.embeddings import embeddings

def create_vectorstore(documents):

    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory="data/chroma_db"
    )

    db.persist()

    return db