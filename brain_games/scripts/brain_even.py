#!/usr/bin/env python3
from random import random
import prompt


def random_number():
    return round(random() * 100)


def welcome():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def answered_user():
    number = random_number()
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    return (answer, number)


def is_corrected():
    answer, number = answered_user()
    if answer == "yes":
        return (number % 2 == 0, answer)
    elif answer == "no":
        return (number % 2 != 0, answer)


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
        print("Entered is an incorrect symbol. The program was finished")


def wrong(flag):
    right_ans = "no" if flag[1] == "yes" else "yes"
    print(f"'{flag[1]}' is wrong answer ;(. Correct answer was '{right_ans}'.")
    print("Let's try again, Bill!")


def main():
    welcome()
    finished()


if __name__ == '__main__':
    main()
