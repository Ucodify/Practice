import os
from dotenv import load_dotenv
import openai 
from llama_index.core import StorageContext, readers
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


load_dotenv()

# Read OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")



# Print partial API key for verification
if api_key:
    print("API key: " + api_key[0:6])
else:
    print("API key not found")


documents = SimpleDirectoryReader("pdf", file_extractor='file_extractor').load_data()


# % % %
# Create the index from the documents
index = VectorStoreIndex.from_documents(documents)
# # Create an index
engine=index.as_query_engine()
result=engine.query("What are the strengths of R over Python?")
print(result)
# # Save the index 
index.storage_context.persist("ml_index")
# % % %




