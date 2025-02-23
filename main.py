from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import requests

    
#Create an instance of the FastAPI class
app=FastAPI()                                           

#Define a route to handle GET requests to the root URL
@app.get("/")                                           
async def read_root():                                  
    return{"message":"Hello World!"}                    
class Item(BaseModel):
    number1:float
    number2:float

app.post("/sum")
async def sum(item:Item):
    return { "result": item.number1 + item.number2 }

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
async def read_root():
    return{"message":"Hello World!"}

# Define the URL
url = "http://127.0.0.1:8000/sum"



# Define the data payload
payload = {
    "num1": 10,
    "num2": 20
}

try:
    # Send POST request
    response = requests.post(url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response text:", response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)