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
    question_expression = f"{number1} {operator} {number2}"
    calculation_value = operators[operator](number1, number2)
    return question_expression, calculation_value
