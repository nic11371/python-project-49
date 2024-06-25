from random import randint


RULE = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(number):
    if number <= 1:
        return "no"
    k = 0
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            k += 1
    return "yes" if k <= 0 else "no"


def make_logic():
    question_expression = randint(1, 100)
    calculation_value = is_prime(question_expression)
    return question_expression, calculation_value
