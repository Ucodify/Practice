from dotenv import load_dotenv
import openai
import os
from llama_index.core import StorageContext, readers
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()

# Read API key and configure OpenAI
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  # Ensure OpenAI library is configured
if api_key:
    print("API key: " + api_key[0:6])
else:
    print("API key not found")


from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)