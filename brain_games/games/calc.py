from random import randint, choice


RULE = "What is the result of the expression?"


def make_logic():
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = choice(list(operators.keys()))
    question_user = f"{number1} {operator} {number2}"
    correct_answer = operators[operator](number1, number2)
    return question_user, correct_answer
