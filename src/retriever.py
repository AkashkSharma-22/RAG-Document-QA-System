from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embedding_model):
    return FAISS.from_documents(chunks, embedding_model)

def get_retriever(db):
    return db.as_retriever(search_kwargs={"k": 2})  # reduced from 3 → faster