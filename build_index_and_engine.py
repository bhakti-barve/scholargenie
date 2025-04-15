from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings import HuggingFaceEmbedding
from langchain_community.llms import Ollama
import os

def load_and_index(path="papers"):
    print("Loading PDFs and building index...")
    documents = SimpleDirectoryReader(input_dir=path).load_data()
    llm = Ollama(model="llama3")
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    return index

