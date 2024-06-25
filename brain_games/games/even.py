from random import randint


RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def make_logic():
    question_expression = randint(1, 100)
    calculation_value = 'yes' if question_expression % 2 == 0 else 'no'
    return question_expression, calculation_value
