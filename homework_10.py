import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'
params = {
    'limit': 150,
}
response = requests.get(url=url, params=params)
result = response.json()
todos = result['todos']

for key in todos:
    if key['completed'] is False:
        pprint(key['todo'])
