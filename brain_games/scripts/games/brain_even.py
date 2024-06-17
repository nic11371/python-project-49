#!/usr/bin/env python3
from random import randint
import prompt


def random_number():
    number = randint(1, 100)
    yes = 'yes'
    no = 'no'
    current_answer = ""
    if number % 2 == 0:
        current_answer = yes
    elif number % 2 != 0:
        current_answer = no
    return (number, current_answer)


def welcome():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def answered_user():
    number = random_number()
    print(f"Question: {number[0]}")
    answer = prompt.string("Your answer: ")
    return (answer, number[1])


def is_corrected():
    answer, even = answered_user()
    if answer == even:
        return (True, answer, even)
    return (False, answer, even)


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
