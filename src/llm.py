from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate


def get_llm():
    return ChatOllama(
        model="phi3",
        temperature=0
    )

def get_prompt():
    template = """
    You are a helpful AI assistant.
    Answer the question using ONLY the provided context.
    Return a clear, concise answer in plain text.
    Do NOT return JSON, bullet points, or any structured format.
    Do NOT include keys like 'answer', 'sources', etc.
    Context:
    {context}
    Question:
    {question}
    Answer:
    """
    return PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
def generate_answer(llm, prompt, context, question):
    formatted_prompt = prompt.format(context=context, question=question)
    response = llm.invoke(formatted_prompt)

    # LangChain AIMessage -> return only assistant text
    if hasattr(response, "content"):
        return response.content.strip()

    # fallback for dict-based responses
    if isinstance(response, dict):
        return str(response.get("answer") or response.get("content") or "").strip()

    return str(response).strip()