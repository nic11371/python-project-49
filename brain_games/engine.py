from prompt import string
from brain_games.cli import welcome


def engine(game_module):
    name_user = welcome()
    print(game_module.RULE)
    count = 3
    while count > 0:
        current_value, corr = game_module.make_logic()
        print(f"Question: {current_value}")
        answer = string("Your answer: ")
        if answer != str(corr):
            print(f"'{answer}' is wrong answer ;(.Correct answer was '{corr}'.")
            print(f"Let's try again, {name_user}!")
            return
        print("Correct")
        count -= 1
    print(f"Congratulations, {name_user}!")
