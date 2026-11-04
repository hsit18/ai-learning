from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

# The class automatically picks up OPENROUTER_API_KEY from the environment
llm = ChatOpenRouter(
    model="openai/gpt-4o",
    temperature=0.7
)

response = llm.invoke("What is the capital of india?")
print(response.content)