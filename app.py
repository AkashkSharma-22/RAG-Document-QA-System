from src.loader import load_pdf
from src.chunker import chunk_docs
from src.embeddings import get_embedding_model
from src.retriever import create_vector_store, get_retriever
from src.llm import get_llm, get_prompt, generate_answer


def main():
    docs = load_pdf("data/sample.pdf")

    # chunking
    chunks = chunk_docs(docs)

    # embeddings + vector db
    emb = get_embedding_model()
    db = create_vector_store(chunks, emb)
    retriever = get_retriever(db)

    # llm + prompt
    llm = get_llm()
    prompt = get_prompt()

    print("✅ Ready! Ask questions (type 'exit' to quit)\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        # retrieve relevant docs
        retrieved_docs = retriever.get_relevant_documents(query)
        context = "\n".join([d.page_content for d in retrieved_docs])

        # generate answer
        answer = generate_answer(llm, prompt, context, query)

        print("\nAnswer:\n", answer, "\n")


if __name__ == "__main__":
    main()