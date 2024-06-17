#!/usr/bin/env python3
import prompt
import brain_games.games.brain_calc as random

messages = {
    "brain-even": "Answer 'yes' if the number is even, otherwise answer 'no'.",
    "brain-calc": "What is the result of the expression?",
}


def welcome_game(message):
    print(message)


def answered_user(data):
    print(f"Question: {data[0]}")
    answer = prompt.string("Your answer: ")
    return (answer, data[1])


def is_corrected():
    answer, expression = answered_user()
    if answer == str(expression):
        return (True, answer, expression)
    return (False, answer, expression)


def finished():

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
    # except TypeError:
    #     print("There is value 'None'. The program was finished")


def wrong(flag):
    print(f"'{flag[1]}' is wrong answer ;(. Correct answer was '{flag[2]}'.")
    print("Let's try again, Bill!")
