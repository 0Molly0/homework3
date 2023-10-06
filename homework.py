import json
import requests

url = 'https://script.google.com/macros/s/AKfycbyPKF1g9ZyQTeAQZ7JuBbUGhfpL9lg2oEC-Fx4mLRS6-lh_DjFcJGyG3F6xQYDVXM4I/exec'

name = requests.get(url)
name_url = name.json()

json_url = json.dumps(name_url)

with open('product.json', mode='w', encoding='utf-8') as file:
    json.dump(name_url, file, indent=4)
