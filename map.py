from list_random import list_random


def list_in_str(item):
    return str(item)


# str_random = map(lambda item: str(item), list_random)
str_random = map(list_in_str, list_random)
print(list(str_random))
