from prompt import string
from brain_games.cli import welcome, welcome_user


def engine(game_module, rules):
    welcome()
    name_user = welcome_user()
    print(rules)
    count = 3
    while count > 0:
        current_value, correct_value = game_module()
        print(f"Question: {current_value}")
        answer_user = string("Your answer: ")
        if answer_user != str(correct_value):
            print(f'''
"{answer_user}" is wrong answer ;(.Correct answer was "{correct_value}".''')
            print(f"Let's try again, {name_user}!")
            break
        print("Correct")
        count -= 1
    else:
        print(f"Congratulations, {name_user}!")
