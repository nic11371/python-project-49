from prompt import string
from brain_games.cli import welcome


MAX_ROUND = 3


def engine(game_module):
    name_user = welcome()
    print(game_module.RULE)
    current_round = 0
    while current_round < MAX_ROUND:
        current_value, correct_value = game_module.make_logic()
        print(f"Question: {current_value}")
        answer_user = string("Your answer: ")
        if answer_user != str(correct_value):
            print(f"'{answer_user}' is wrong answer ;(.Correct answer was '{correct_value}'.")
            print(f"Let's try again, {name_user}!")
            return
        print("Correct")
        current_round += 1
    print(f"Congratulations, {name_user}!")
