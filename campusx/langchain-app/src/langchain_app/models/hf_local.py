from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = './huggingface_cache'

DEFAULT_CONFIG = {
    "model_id":'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    "task":'text-generation',
    "pipeline_kwargs":dict(
        temperature=0.5,
        max_new_tokens=100
    )
}

def get_model(config: dict | None = None) -> ChatHuggingFace:
    """Build a huggingface local model, overriding any default with `config`.
    """
    llm = HuggingFacePipeline.from_model_id(**{**DEFAULT_CONFIG, **(config or {})})
    return ChatHuggingFace(llm=llm)