import requests


url = "https://api.trello.com/1/boards/"

query = {
    "key": "fb392e20ec73ead3cb6fe326917cb9b8",
    "token": "b1d147dce6701c17ca339bd7680aaf0e0a4f93f3a8d854d40fde155cc90a41e7",
    "name": "newboard",
}

response = requests.request("POST", url, params=query)
print(response.text)


url = "https://api.trello.com/1/cards"

query = {
    "key": "fb392e20ec73ead3cb6fe326917cb9b8",
    "token": "b1d147dce6701c17ca339bd7680aaf0e0a4f93f3a8d854d40fde155cc90a41e7",
    "idList": "5f046dc62d3dfa18edeec08e",
}

response = requests.request("POST", url, params=query)
print(response.text)
