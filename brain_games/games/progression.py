from random import randint, choice


RULE = "What number is missing in the progression?"


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
    for index, value in enumerate(sequence):
        if value == hidden_number:
            sequence[index] = ".."
    question = " ".join(str(x) for x in sequence)
    return question, hidden_number
