import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint,params={"abc": 123})
print(get_response.json())
