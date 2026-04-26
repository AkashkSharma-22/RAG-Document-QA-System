# 📄 RAG Document QA System

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-121212?style=flat-square&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)](https://ollama.com/)

A professional, privacy-focused Retrieval-Augmented Generation (RAG) system that allows users to chat with their PDF documents locally. Powered by **Ollama (Phi-3)**, **LangChain**, and **FAISS**, this application ensures your data never leaves your machine.

---

## ✨ Key Features

- **100% Local Execution:** Privacy-first approach using Ollama for local LLM inference.
- **Smart Document Processing:** Efficient PDF text extraction and semantic chunking.
- **Fast Retrieval:** Utilizes FAISS (Facebook AI Similarity Search) for high-performance vector search.
- **Modern UI:** Clean and intuitive chat interface built with Streamlit.
- **Optimized Performance:** Uses lightweight embeddings (`all-MiniLM-L6-v2`) for quick response times.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Orchestration:** [LangChain](https://www.langchain.com/)
- **LLM:** [Ollama](https://ollama.com/) (Model: `phi3`)
- **Vector Store:** [FAISS](https://github.com/facebookresearch/faiss)
- **Embeddings:** [HuggingFace](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Document Loader:** PyPDF

---

## 🏗️ Architecture Overview

The system follows a standard RAG (Retrieval-Augmented Generation) pipeline:

1.  **Ingestion:** PDF documents are loaded and split into manageable chunks.
2.  **Embedding:** Each chunk is converted into a numerical vector using a Transformer-based embedding model.
3.  **Indexing:** Vectors are stored in a FAISS index for efficient similarity searching.
4.  **Retrieval:** When a user asks a question, the system finds the most relevant document chunks.
5.  **Generation:** The retrieved context and the user's question are sent to the local Phi-3 model to generate a precise answer.

---

## 🚀 Installation

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) installed and running.

### Step-by-Step Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/AkashkSharma-22/RAG-Document-QA-System.git
    cd RAG-Document-QA-System
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Pull the LLM Model:**
    Ensure Ollama is running, then execute:
    ```bash
    ollama pull phi3
    ```

---

## 📖 Usage

### 🌐 Web Interface (Recommended)
1.  **Start the Application:**
    ```bash
    streamlit run streamlit_app.py
    ```
2.  **Upload a Document:** Use the interface to upload a PDF file.
3.  **Chat:** Once processed, start asking questions about your document.

### 💻 CLI Interface
For a lightweight terminal-based experience:
1.  Place your PDF in the `data/` folder and name it `sample.pdf`.
2.  Run the script:
    ```bash
    python app.py
    ```
3.  Type your questions and get instant answers. Type `exit` to quit.

### Example
**User:** "What are the main findings of this report?"
**Assistant:** "Based on the provided document, the main findings include... [details from the PDF]"

---

## 📁 Project Structure

```text
RAG-Document-QA-System/
├── src/
│   ├── loader.py        # PDF loading logic
│   ├── chunker.py       # Text splitting strategies
│   ├── embeddings.py    # Embedding model configuration
│   ├── retriever.py     # FAISS vector store and retrieval
│   └── llm.py           # Ollama integration and prompt templates
├── data/                # Sample data for testing
├── app.py               # (Optional) Main entry point
├── streamlit_app.py     # Streamlit UI implementation
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```


## 🚀 Future Improvements

- [ ] Support for multiple file formats (DOCX, TXT, CSV).
- [ ] Implementation of persistent vector storage (ChromaDB/Pinecone).
- [ ] Advanced RAG techniques: Hybrid search and Re-ranking.
- [ ] Multi-document chat capabilities.
- [ ] Integration with more local models (Llama 3, Mistral).

---

## 🤝 Contribution

Contributions are welcome! Please follow these steps:
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---


