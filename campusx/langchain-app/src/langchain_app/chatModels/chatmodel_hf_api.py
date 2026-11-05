from langchain_app.models.hf_api import get_model

model = get_model()
result = model.invoke("What is the capital of india?")
print(result.content)