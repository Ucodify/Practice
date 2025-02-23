import os
from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Read OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Validate API key
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

# Load index from storage
try:
    storage_context = StorageContext.from_defaults(persist_dir="ml_index")
    index = load_index_from_storage(storage_context)
    engine = index.as_query_engine()
except Exception as e:
    raise RuntimeError(f"Failed to load index: {e}")

# FastAPI setup
app = FastAPI()

class Item(BaseModel):
    question: str

@app.post("/")
async def query(item: Item):
    try:
        result = engine.query(item.question)
        return {"answer": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {e}")

# Run the server
if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
