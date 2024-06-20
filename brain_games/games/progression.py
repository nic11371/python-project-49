from random import randint, choice


def logic_function():
    sequence = []
    start = randint(1, 10)
    stop = randint(6, 10)
    step = randint(1, 10)
    for i in range(stop):
        value = start + step
        sequence.append(value)
        start = value
    question = " ".join(str(x) for x in sequence)
    hidden_number = choice(sequence)
    if str(hidden_number) in question:
        question = question.replace(str(hidden_number), "..")
    return (question, hidden_number)
