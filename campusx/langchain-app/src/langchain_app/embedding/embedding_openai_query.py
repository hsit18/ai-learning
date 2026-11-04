from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
embedding = OpenAIEmbeddings(
    model="openai/text-embedding-3-small",         # Replace with any OpenRouter embedding model
    openai_api_key=os.environ.get("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1", # Crucial endpoint redirection
    dimensions=32
)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))