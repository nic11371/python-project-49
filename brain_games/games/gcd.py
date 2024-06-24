from random import randint
from math import gcd


RULE = "Find the greatest common divisor of given numbers."


def make_logic():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f"{number1} {number2}"
    calculation = gcd(number1, number2)
    return question, calculation
