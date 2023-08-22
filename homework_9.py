import requests
from pprint import pprint

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
result = response.json()
people = result['people']

person, value, *other = people
list_people = []

for person in people:
    if person['craft']:
        list_people.append([person['name']])
pprint(list(list_people))
