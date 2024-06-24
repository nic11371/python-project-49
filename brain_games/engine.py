from prompt import string
from brain_games.cli import welcome


MAX_ROUND = 3


def engine(game_module):
    name_user = welcome()
    print(game_module.RULE)
    current_round = 0
    while current_round < MAX_ROUND:
        current_value, corr = game_module.make_logic()
        print(f"Question: {current_value}")
        answer = string("Your answer: ")
        if answer != str(corr):
            print(f"'{answer}' is wrong answer ;(.Correct answer was '{corr}'.")
            print(f"Let's try again, {name_user}!")
            return
        print("Correct")
        current_round += 1
    print(f"Congratulations, {name_user}!")
