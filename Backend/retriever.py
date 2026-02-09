from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from llm import get_response

embeddings = OllamaEmbeddings(
    model="llama3.2:1b",
)

url="your_url" 
api_key="your_api_key"

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="cyber security",
    url=url,
    api_key=api_key,
)

def get_answer(question: str) -> str:
    """
    Takes a question, retrieves relevant context from Qdrant, and returns an answer.
    
    Args:
        question (str): The user's question
        
    Returns:
        str: The chatbot's answer
    """
    # Retrieve relevant chunks from Qdrant
    results = qdrant.similarity_search(
        question, k=2
    )
    
    # Create prompt with question and context
    prompt = f"""
question: {question}
context: {results}
"""
    
    # Get response from LLM
    answer = get_response(prompt)
    return answer


# For testing: if script is run directly, use input()
if __name__ == "__main__":
    question = input("Enter your question: ")
    answer = get_answer(question)
    print("Answer: ", answer)