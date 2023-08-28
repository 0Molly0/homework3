from homework_12 import string_in_list
from pywebio.input import input as pw_input
from pywebio.output import put_text


user_text = pw_input('Enter your text: ')
put_text(string_in_list(user_text))
