def string_in_list(text: str) -> list:
    list_1 = []
    number = 0
    while number < len(text) and len(list_1) < 100:
        char = text[number]
        if char not in ['m', 'n']:
            list_1.append(char.upper()), ', '.join(list_1)
        number += 1
    return list_1
