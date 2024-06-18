import prompt


messages = {
    "even": "Answer 'yes' if the number is even, otherwise answer 'no'.",
    "calc": "What is the result of the expression?",
    "gcd": "Find the greatest common divisor of given numbers."
}


def engine(game_module):
    welcome_game(messages[game_module.__name__[18:]])
    count = 3
    while count > 0:
        number, answer_module = game_module.logic_function()
        answer_user, answer_module = user(number, answer_module)
        boolean, current, correct = is_corrected(answer_user, answer_module)
        if boolean is not True:
            wrong(current, correct)
            break
        print("Correct")
        count -= 1
    else:
        print("Congratulations, Bill!")


def welcome_game(message):
    print(message)


def user(number, answer_module):
    print(f"Question: {number}")
    answer_user = prompt.string("Your answer: ")
    return (answer_user, answer_module)


def is_corrected(answer_user, answer_module):
    if answer_user == str(answer_module):
        return (True, answer_user, answer_module)
    return (False, answer_user, answer_module)


def wrong(current, correct):
    print(f"'{current}' is wrong answer ;(. Correct answer was '{correct}'.")
    print("Let's try again, Bill!")
