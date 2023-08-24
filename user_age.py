def check_age(age: int) -> str:
    if age <= 0:
        return '\U0000274C You have entered the wrong age because the age cannot be lower than 0 \U0000274C'
    elif 1 <= age <= 18:
        return '\U0001F476 You are a child! \U0001F476'
    elif 19 <= age <= 65:
        return '\U0001F477 GO TO WORK! \U0001F477'
    else:
        return '\U0001F474 Happy retirement! \U0001F475'
