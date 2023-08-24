from user_age import check_age


def test_negative_age():
    expected_result = '\U0000274C You have entered the wrong age because the age cannot be lower than 0 \U0000274C'
    age = -5
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_child_age():
    expected_result = '\U0001F476 You are a child! \U0001F476'
    age = 15
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_work_age():
    expected_result = '\U0001F477 GO TO WORK! \U0001F477'
    age = 25
    actual_result = check_age(age)
    assert actual_result == expected_result


def test_elderly_age():
    expected_result = '\U0001F474 Happy retirement! \U0001F475'
    age = 78
    actual_result = check_age(age)
    assert actual_result == expected_result
