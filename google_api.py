import requests

url = 'https://script.google.com/macros/s/AKfycbyPKF1g9ZyQTeAQZ7JuBbUGhfpL9lg2oEC-Fx4mLRS6-lh_DjFcJGyG3F6xQYDVXM4I/exec'

name = requests.get(url)
name_dict = name.json()

money = 0

price = sum([product['price'] for product in name_dict['product'] if product['price']])
sum_money = f'Вартість всіх товарів = {price}'
print(sum_money)

price_not_gluten_products = sum([product['price'] for product in name_dict['product'] if product['contains gluten'] is True])
sum_money_contains_gluten = f'Вартість товарів без глютена = {price_not_gluten_products}'
print(sum_money_contains_gluten)
