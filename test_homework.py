from homework_12 import string_in_list
from homework_13 import vehicle_description


def test_string_in_list():
    input_text = str('a' * 150)
    expected_output = list('A' * 100)
    actual_result = string_in_list(input_text)
    assert actual_result == expected_output


def test_vehicle_description():

    actual_result = vehicle_description(speed=3, time=10, weight=1000)

    expected_result = f"Транспортний засіб вагою 1000 кг рухався 10 секунд зі швидкістю 3 м/сек, " \
                      f"і подолав відстань 30 метрів"

    assert expected_result == actual_result
