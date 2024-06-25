from prompt import string
from brain_games.cli import welcome


MAX_ROUND = 3


def engine(game_module):
    name_user = welcome()
    print(game_module.RULE)
    current_round = 0
    while current_round < MAX_ROUND:
        question_user, correct_answer = game_module.make_logic()
        print(f"Question: {question_user}")
        answer = string("Your answer: ")
        if answer != str(correct_answer):
            print(
                f'''"{answer}" is wrong answer ;(.
Correct answer was "{correct_answer}".'''
            )
            print(f"Let's try again, {name_user}!")
            return
        print("Correct")
        current_round += 1
    print(f"Congratulations, {name_user}!")
