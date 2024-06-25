from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv
import os

def load_documents():
    # Load documents from the "data" directory
    documents = SimpleDirectoryReader("data").load_data()
    return documents

def create_index(documents):
    # Create a vector store index from the documents
    index = VectorStoreIndex.from_documents(documents)
    return index

def get_query_engine():
    # Load the environment variables
    load_dotenv()
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    # Load documents and create index
    documents = load_documents()
    index = create_index(documents)
    
    # Create and return a query engine from the index
    return index.as_query_engine()

def get_response(query):
    query_engine = get_query_engine()
    response = query_engine.query(query)
    return response
