from random import randint


def logic_function():
    number = randint(1, 100)
    k = 0
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            k += 1
    if k <= 0:
        current_answer = "yes"
    else:
        current_answer = "no"
    return (number, current_answer)
