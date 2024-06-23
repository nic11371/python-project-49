from random import randint


RULE = "Find the greatest common divisor of given numbers."


def found_divide():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f"{number1} {number2}"
    tmp = number2 if number1 > number2 else number1
    for i in range(1, tmp + 1):
        if ((number1 % i == 0) and (number2 % i == 0)):
            gcd = i
    calculation = gcd
    return question, calculation
