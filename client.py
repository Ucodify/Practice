import requests

# Define the URL
url = "http://127.0.0.1:8000"

# Define the payload with a string query
data = {"query": "Why Choose Python over R?, server!"}

try:
    # Make the POST request
    response = requests.post(url, json=data)
    
    # Check if the request was successful
    response.raise_for_status
    
    # Print the response JSON
    result = response.json()
    print("Response:", result)
except requests.exceptions.RequestException as e:
    print("Error:", e)