from langchain_community.document_loaders import PyPDFLoader

file_path = "your pdf filepath"
loader = PyPDFLoader(file_path)

docs = loader.load_and_split()
print(len(docs))

from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

embeddings = OllamaEmbeddings(
    model="llama3.2:1b",
)

from qdrant_client import QdrantClient


url="your_url" 
api_key="your_api_key"


qdrant = QdrantVectorStore.from_documents(
    docs,
    embeddings,
    url=url,
    api_key=api_key,
    collection_name="cyber security",
)
