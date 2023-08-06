from pywebio.input import input as pw_input
from pywebio.output import put_success, put_warning, put_code, put_markdown, popup

unwanted_chars = '0987654321()-_.,:;!? '

user_favorite_animal = str(pw_input('Введіть назву улюбленої тварини', required=True)).casefold().strip(unwanted_chars)
put_success(user_favorite_animal)

user_pets_name = str(pw_input('Введіть кличку вашего улюбленця', required=True)).strip(unwanted_chars).title()
put_warning(user_pets_name)

cat_emodji = '\U0001F408'
dog_emodji = '\U0001F436'
fish_emodji = '\U0001F420'
hamster_emodji = '\U0001F439'
turtle_emodji = '\U0001F422'

user_pet_swimming = str(pw_input('Ваш улюбленець може плавати? (так/ні)', required=True))

fish = 'риба'
turtle = 'черепаха'

can_swim = user_favorite_animal == fish or user_favorite_animal == turtle
cant_swim = not can_swim

if can_swim:
    put_code('Ваш улюбленець вміє плавати')
    put_markdown('Вам потрібно купити акваріум')
else:
    put_code('Ваш улюбленець не може плавати ')

if user_favorite_animal == 'собака':
    popup(f'Я боюся гавкоту собак, в тому числі {user_pets_name} {dog_emodji}')
elif user_favorite_animal == 'кіт':
    popup(f'Коти ловлять мишей {cat_emodji}')
elif user_favorite_animal == 'хомяк':
    popup(f'Хомячки маленькі {hamster_emodji}')
elif user_favorite_animal == 'риба':
    popup(f'Рибку не смажити {fish_emodji}')
elif user_favorite_animal == 'черепаха':
    popup(f'У черепахи міцний панцир {turtle_emodji}')
else:
    popup('Я не знаю тип наданої тварини \U0001F61E ')
