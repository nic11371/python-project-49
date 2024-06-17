#!/usr/bin/env python3
from random import randint
import brain_games.engine as engine


def random_expression():
    number = randint(1, 100)
    yes = 'yes'
    no = 'no'
    current_answer = ""
    if number % 2 == 0:
        current_answer = yes
    elif number % 2 != 0:
        current_answer = no
    return (number, current_answer)


def main():
    engine.welcome_game(engine.messages["brain-even"])
    engine.finished()


if __name__ == '__main__':
    main()
