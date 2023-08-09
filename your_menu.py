from decimal import Decimal
from pywebio.input import slider
from pywebio.output import put_code, popup, put_warning

OSTRICH_EGG = 118
RABBIT = 197
SEA_BASS = 123
SWEET_RED_PEPPER = 26
PARSLEY = 45
BANANAS = 87
WAFFLES = 425
WHEAT_BREAD_FROM_GRADE_1_FLOUR = 329
PISTACHIOS = 555
KEFIR = 51

PRICE_PER_CALORIE = 0.32541
total_calories = 0

weight_ostrich_egg = slider(f'Введіть порцію строусиного яйця \U0001F95A  в грамах.'
                            f' Калорійність {OSTRICH_EGG} кКал/100гр', min_value=0, max_value=1000)
total_calories += weight_ostrich_egg * OSTRICH_EGG / 100
put_code(f'Ви замовили {weight_ostrich_egg} грамів страусиних яєць,\n'
         f'Калорійність порції {weight_ostrich_egg * OSTRICH_EGG / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_rabbit = slider('Введіть порцію кролика \U0001F407 в грамах. '
                       f'Калорійність {RABBIT} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_rabbit * RABBIT / 100
put_code(f'Ви замовили {weight_rabbit} грамів кролика,\n'
         f'Калорійність порції {weight_rabbit * RABBIT / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_sea_bass = slider('Введіть порцію окуня морського \U0001F41F в грамах. '
                         f'Калорійність {SEA_BASS} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_sea_bass * SEA_BASS / 100
put_code(f'Ви замовили {weight_sea_bass} грамів окуня морського,\n'
         f'Калорійність порції {weight_sea_bass * SEA_BASS / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_sweet_red_pepper = slider('Введіть порцію перця червоного солодкого в грамах. '
                                 f'Калорійність {SWEET_RED_PEPPER} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_sweet_red_pepper * SWEET_RED_PEPPER / 100
put_code(f'Ви замовили {weight_sweet_red_pepper} грамів перця червоного солодкого,\n'
         f'Калорійність порції {weight_sweet_red_pepper * SWEET_RED_PEPPER / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_parsley = slider('Введіть порцію петрушки(зелені) 🌿 в грамах. '
                        f'Калорійність {PARSLEY} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_parsley * PARSLEY / 100
put_code(f'Ви замовили {weight_parsley} грамів петрушки(зелені),\n'
         f'Калорійність порції {weight_parsley * PARSLEY / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_bananas = slider('Введіть порцію бананів \U0001F34C  в грамах. '
                        f'Калорійність {BANANAS} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_bananas * BANANAS / 100
put_code(f'Ви замовили {weight_bananas} грамів бананів,\n'
         f'Калорійність порції {weight_bananas * BANANAS / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_waffles = slider('Введіть порцію вафлів \U0001F9C7 в грамах. '
                        f'Калорійність {WAFFLES} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_waffles * WAFFLES / 100
put_code(f'Ви замовили {weight_waffles} грамів вафлів,\n'
         f'Калорійність порції {weight_waffles * WAFFLES / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_wheat_bread_from_grade_1_flour = slider('Введіть порцію хліба пшенічного 1 сорту \U0001F956 в грамах. '
                                               f'Калорійність {WHEAT_BREAD_FROM_GRADE_1_FLOUR} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_wheat_bread_from_grade_1_flour * WHEAT_BREAD_FROM_GRADE_1_FLOUR / 100
put_code(f'Ви замовили {weight_wheat_bread_from_grade_1_flour} грамів хліба пшенічного 1 сорту,\n'
         f'Калорійність порції {weight_wheat_bread_from_grade_1_flour * WHEAT_BREAD_FROM_GRADE_1_FLOUR / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_pistachios = slider('Введіть порцію фісташок в грамах. '
                           f'Калорійність {PISTACHIOS} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_pistachios * PISTACHIOS / 100
put_code(f'Ви замовили {weight_pistachios} грамів фісташок,\n'
         f'Калорійність порції {weight_pistachios * PISTACHIOS / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

weight_kefir = slider('Введіть порцію кефіра \U0001F95B в грамах. '
                      f'Калорійність {KEFIR} кКал/100гр', min_value=0, max_value=500)
total_calories += weight_kefir * KEFIR / 100
put_code(f'Ви замовили {weight_kefir} грамів кефіра,\n'
         f'Калорійність порції {weight_kefir * KEFIR / 100} кКал \n'
         f'Загальна калорійність порції: {total_calories} кКал')

if total_calories < 1000:
    popup('Ви, мабудь залишитеся голодним.\U0001F61E')
elif total_calories > 1500:
    popup('На жаль, ви стільки не зїсте, і це все гроші в смітник')
else:
    popup('Це саме ваш варіант вечері')

counting_total_price = PRICE_PER_CALORIE * total_calories
total_price = Decimal(str(counting_total_price)).quantize(Decimal('0.01'))
put_warning(f'Загальна вартість замовлення {total_price} грн')
