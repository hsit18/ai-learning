import os
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
model = os.getenv("MODEL", "anthropic/claude-sonnet-4.6")
# The SDK automatically reads ANTHROPIC_BASE_URL and ANTHROPIC_AUTH_TOKEN from your environment
client = Anthropic()