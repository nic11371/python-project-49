#!/usr/bin/env python3
from random import randint, choice
import prompt


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


def welcome():
    print("What is the result of the expression?")


def answered_user():
    expression = random_expression()
    print(f"Question: {expression[0]}")
    answer = prompt.string("Your answer: ")
    return (answer, expression[1])


def is_corrected():
    answer, expression = answered_user()
    if answer == str(expression):
        return (True, answer, expression)
    return (False, answer, expression)


def finished():
    try:
        count = 3
        while count > 0:
            is_flag = is_corrected()
            if is_flag[0] is not True:
                wrong(is_flag)
                break
            print("Correct")
            count -= 1
        else:
            print("Congratulations, Bill!")
    except TypeError:
        print("There is value 'None'. The program was finished")


def wrong(flag):
    print(f"'{flag[1]}' is wrong answer ;(. Correct answer was '{flag[2]}'.")
    print("Let's try again, Bill!")


def main():
    welcome()
    finished()


if __name__ == '__main__':
    main()
