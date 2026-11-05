from langchain_app.models.openrouter import get_model

model = get_model()

response = model.invoke("What is the capital of india?")
print(response)