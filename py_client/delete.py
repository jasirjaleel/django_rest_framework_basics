import requests

endpoint = "http://localhost:8000/api/products/3/destroy/"

get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code==204)
