from langchain_app.models.openrouter import get_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


model = get_model()

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
