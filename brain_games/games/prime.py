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
    question_user = randint(1, 100)
    correct_answer = is_prime(question_user)
    return question_user, correct_answer
