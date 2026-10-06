import os
from dotenv import load_dotenv

load_dotenv()
from groq_models import Groq

# Initialize client (uses GROQ_API_KEY environment variable)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Fetch all available models
models = client.models.list()

print("Available Groq Models:\n")
for model in models.data:
    if model.active:
        print(f"- {model.id}")