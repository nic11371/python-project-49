from random import randint


RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def make_logic():
    question_user = randint(1, 100)
    correct_answer = 'yes' if question_user % 2 == 0 else 'no'
    return question_user, correct_answer
