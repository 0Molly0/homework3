import certifi
import pymongo

from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}@cluster0.0tgfhp0.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url, tlsCAFile=certifi.where())

db = client.book
fantasy_book_coll = db.fantasy_book
school_literature_coll = db.school_literature

# fantasy_book_coll.insert_one({'_id': 19, 'name': 'Гра престолів', 'price': 775, 'year': 2019, 'number_of_pages': 800})

school_literature = [
    {'_id': '1', 'name': 'Основи правознавства', 'class': 9, 'number_of_pages': 191, 'data': 2017},
    {'_id': '2', 'name': 'Українська література', 'class': 9, 'number_of_pages': 335, 'data': 2017},
    {'_id': '3', 'name': 'Історія України', 'class': 9, 'number_of_pages': 287, 'data': 2017},
    {'_id': '4', 'name': 'Географія', 'class': 9, 'number_of_pages': 271, 'data': 2017},
    {'_id': '5', 'name': 'Фізика', 'class': 9, 'number_of_pages': 279, 'data': 2022},
    {'_id': '6', 'name': 'Всесвітня історія', 'class': 9, 'number_of_pages': 256, 'data': 2017},
]
# school_literature_coll.insert_many(school_literature)


query = {'name': {'$regex': '[Іі]сторія'}}
result = school_literature_coll.find(query)
for doc in result:
    print(doc)

# current = {'name': 'Гра престолів'}
# new_price = {'$inc': {'price': 56}}
# price = fantasy_book_coll.update_one(current, new_price)

delete = fantasy_book_coll.delete_one({'name': 'Гра престолів'})

query = {'data': {'$lt': 2020}}
delete_book = school_literature_coll.delete_many(query)
