from homework_13 import vehicle_description

user_time = int(input('Time: '))
user_speed = int(input('Speed: '))
user_weight = int(input('Weight: '))
description = vehicle_description(time=user_time, speed=user_speed, weight=user_weight)

print(description)

# description
