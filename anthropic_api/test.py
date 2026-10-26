import os
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
model = os.getenv("MODEL", "anthropic/claude-sonnet-4.6")
# The SDK automatically reads ANTHROPIC_BASE_URL and ANTHROPIC_AUTH_TOKEN from your environment
client = Anthropic()

# response = client.messages.create(
#     # Use the OpenRouter identifier prefix for Anthropic models
#     model=model, 
#     max_tokens=1024,
#     messages=[
#         {"role": "user", "content": "Hello Claude, via OpenRouter!"}
#     ]
# )


message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)
print(message.content[0].text)