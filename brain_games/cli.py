from prompt import string


def welcome():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = string("May I have your name? ")
    print(f"Hello, {name}")
    return name
