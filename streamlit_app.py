import streamlit as st

from src.loader import load_pdf
from src.chunker import chunk_docs
from src.embeddings import get_embedding_model
from src.retriever import create_vector_store, get_retriever
from src.llm import get_llm, get_prompt, generate_answer

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("📄 Chat with your Document (RAG + phi3)")

# session state init
if "messages" not in st.session_state:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    st.session_state.retriever = None

# upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded!")

    # process only once
    if st.session_state.retriever is None:
        with st.spinner("Processing document..."):
            docs = load_pdf("temp.pdf")
            chunks = chunk_docs(docs)

            emb = get_embedding_model()
            db = create_vector_store(chunks, emb)

            st.session_state.retriever = get_retriever(db)
            st.session_state.llm = get_llm()
            st.session_state.prompt = get_prompt()

        st.success("Ready! Ask your questions below 👇")

# show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# chat input
if user_input := st.chat_input("Ask something about your document..."):

    if st.session_state.retriever is None:
        st.warning("⚠️ Please upload a PDF first.")
    else:
        # show user msg
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # retrieve context
        retrieved_docs = st.session_state.retriever.invoke(user_input)
        context = "\n".join([d.page_content for d in retrieved_docs])

        # generate response
        with st.spinner("Thinking..."):
            answer = generate_answer(
                st.session_state.llm,
                st.session_state.prompt,
                context,
                user_input
            )

        # show assistant msg
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)