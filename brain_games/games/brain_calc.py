#!/usr/bin/env python3
from random import randint, choice
import brain_games.engine as engine


def random_expression():
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operator = choice(list(operators.keys()))
    question = f"{number1} {operator} {number2}"
    calculation = operators[operator](number1, number2)
    return (question, calculation)


def main():
    engine.welcome_game(engine.messages["brain-calc"])
    function_random = random_expression()
    engine.answered_user(function_random)
    engine.finished()


if __name__ == '__main__':
    main()
