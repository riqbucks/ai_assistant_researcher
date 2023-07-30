import requests

response = requests.post(
    'http://127.0.0.1:10000',  # Use the loopback address
    json={
        "query": "what is the meta's new product Thread"  
    }
)

print(response.json())
