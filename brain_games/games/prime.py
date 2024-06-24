from random import randint


RULE = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def make_logic():
    number = randint(1, 100)
    k = 0
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            k += 1
    if k <= 0:
        current_answer = "yes"
    else:
        current_answer = "no"
    return number, current_answer
