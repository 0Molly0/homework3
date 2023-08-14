from pywebio.input import input as pw_input
from pywebio.output import put_code

was_in_cities = set(pw_input('Введіть через пробіл міста, в якіх ви були за минулі 10 років:').split())

the_city_you_want_to_go_to = set(pw_input('Введіть через пробіл міста, в які ви хочете поїхати внаступні 10 років:').split())

common = was_in_cities & the_city_you_want_to_go_to
string_common = ', '.join(common)

if common:
    put_code(f'Вам, мабуть, дуже сподобалося в ціх містах: {string_common}')
else:
    put_code('Ви відкриті до чогось нового \U0001F60A')
