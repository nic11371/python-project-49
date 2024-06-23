from prompt import string
from brain_games.cli import welcome, welcome_user


def engine(game_module, rules):
    welcome()
    name_user = welcome_user()
    welcome_game(rules)
    count = 3
    while count > 0:
        number, answer_module = game_module()
        answer_user, answer_module = user(number, answer_module)
        boolean, current, correct = is_corrected(answer_user, answer_module)
        if boolean is not True:
            wrong(current, correct, name_user)
            break
        print("Correct")
        count -= 1
    else:
        print(f"Congratulations, {name_user}!")


def welcome_game(message):
    print(message)


def user(number, answer_module):
    print(f"Question: {number}")
    answer_user = string("Your answer: ")
    return (answer_user, answer_module)


def is_corrected(answer_user, answer_module):
    if answer_user == str(answer_module):
        return (True, answer_user, answer_module)
    return (False, answer_user, answer_module)


def wrong(current, correct, name_user):
    print(f"'{current}' is wrong answer ;(. Correct answer was '{correct}'.")
    print(f"Let's try again, {name_user}!")
