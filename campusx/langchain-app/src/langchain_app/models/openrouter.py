from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

DEFAULT_CONFIG = {
    "model": "openai/gpt-4o",
    "temperature": 0.7,
}


def get_model(config: dict | None = None) -> ChatOpenRouter:
    """Build a ChatOpenRouter, overriding any default with `config`.

    The class automatically picks up OPENROUTER_API_KEY from the environment.
    """
    return ChatOpenRouter(**{**DEFAULT_CONFIG, **(config or {})})
