import os
from anthropic import Anthropic
import voyageai
from dotenv import load_dotenv
load_dotenv()
model = os.getenv("MODEL", "anthropic/claude-sonnet-4.6")
# The SDK automatically reads ANTHROPIC_BASE_URL and ANTHROPIC_AUTH_TOKEN from your environment
client = Anthropic()

voClient = voyageai.Client(
    api_key=os.getenv("ANTHROPIC_AUTH_TOKEN"), 
    base_url="https://openrouter.ai/api/v1"
)