from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

DEFAULT_CONFIG = {
    "repo_id":"TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "task":"text-generation"
}

def get_model(config: dict | None = None) -> ChatHuggingFace:
    """Build a huggingface inferance API, overriding any default with `config`.
    """

    llm = HuggingFaceEndpoint(**{**DEFAULT_CONFIG, **(config or {})})

    return ChatHuggingFace(llm=llm)
