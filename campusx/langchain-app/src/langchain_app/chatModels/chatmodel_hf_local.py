from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_app.models.hf_local import get_model

model = get_model()

result = model.invoke("What is the capital of India")

print(result.content)