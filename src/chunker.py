from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30
    )
    return splitter.split_documents(docs)