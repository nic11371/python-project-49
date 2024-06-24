from random import randint


RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def make_logic():
    number = randint(1, 100)
    current_answer = 'yes' if number % 2 == 0 else 'no'
    return number, current_answer
