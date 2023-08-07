import requests

endpoint = "http://localhost:8000/api/"

# get_response = requests.post(endpoint + "/login/", json={
#     "uid": "rEbghNFymyX2nCaifrH2iSj64bE3"
# })

# print(get_response.status_code)

get_response = requests.post(endpoint, json={'content': 'hello world', 'title': None, 'discount': 0.5})
# print(get_response.headers)
# print(get_response.text)
print(get_response.json())