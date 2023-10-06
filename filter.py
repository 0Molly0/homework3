from list_random import list_random


def random_numbers(item):
    return isinstance(item, int)


int_random = filter(random_numbers, list_random)
print(list(int_random))
