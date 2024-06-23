from random import randint


def logic_function():
    number = randint(1, 100)
    current_answer = ""
    if number % 2 == 0:
        current_answer = 'yes'
    elif number % 2 != 0:
        current_answer = 'no'
    return number, current_answer
