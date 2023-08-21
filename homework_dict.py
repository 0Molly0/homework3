from pprint import pprint
from decimal import Decimal

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

ayanami_rei = {
    'Пошта': 'Rei@gmail.com',
    'Вік': 20,
    'Номер телефону': '+380987601221',
    'Середній бал': 10}

students.setdefault('Аянамі Рей', ayanami_rei)

list_of_students = []
key, value, *other_data = students
total_score = 0

for key, value in students.items():
    if students[key]['Середній бал'] > 90:
        list_of_students = key, students[key]
    total_score += students[key]['Середній бал']
    if not students[key]['Номер телефону']:
        students[key]['Номер телефону'] = '+380997971821'
pprint(list(list_of_students))

final_score = Decimal(total_score / len(students)).quantize(Decimal('0.01'))
print(f'Cередній бал групи = {final_score}')

pprint(students)
