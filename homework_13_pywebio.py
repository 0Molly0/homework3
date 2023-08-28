from pywebio.input import input as pw_input
from pywebio.output import put_success
from pywebio.input import FLOAT
from homework_13 import vehicle_description

user_time = int(pw_input('Time: ', FLOAT))
user_speed = int(pw_input('Speed: ', FLOAT))
user_weight = int(pw_input('Weight: ', FLOAT))
description = vehicle_description(time=user_time, speed=user_speed, weight=user_weight)

put_success(description)
