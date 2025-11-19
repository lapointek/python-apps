import requests
import os

USERNAME = os.environ.get("HT_USERNAME")
TOKEN = os.environ.get("HT_TOKEN")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
