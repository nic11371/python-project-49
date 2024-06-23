from random import randint, choice


def logic_function():
    sequence = []
    start = randint(0, 10)
    stop = randint(5, 10)
    step = randint(1, 10)
    for i in range(stop):
        value = start + step
        sequence.append(value)
        start = value
    hidden_number = choice(sequence)
    question = " ".join(str(x) for x in sequence)
    if hidden_number in sequence:
        question = question.replace(str(hidden_number), "..")
    return question, hidden_number
