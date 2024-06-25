from random import randint
from math import gcd


RULE = "Find the greatest common divisor of given numbers."


def make_logic():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question_expression = f"{number1} {number2}"
    calculation_value = gcd(number1, number2)
    return question_expression, calculation_value
