from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import os

def get_chroma_memory():
    persist_dir = os.path.join(os.getcwd(), "memory_db")
    embedding_model = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    return Chroma(persist_directory=persist_dir, embedding_function=embedding_model)
