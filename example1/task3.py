import requests


def getData():
    request = requests.get('https://jsonplaceholder.typicode.com/users')
    print(request.json())

