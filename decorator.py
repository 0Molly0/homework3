def decorator_1(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        text = str(text)
        return text
    return wrapper


@decorator_1
def convert_to_str(value1: str, value2: str) -> str:
    return value1 + value2


result = convert_to_str(value1='I ', value2='eat! \U0001F354')
print(result)
