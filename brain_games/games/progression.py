from random import randint, choice


RULE = "What number is missing in the progression?"


def make_logic():
    sequence = []
    start = randint(0, 10)
    stop = randint(5, 10)
    step = randint(1, 10)
    for i in range(stop):
        value = start + step
        sequence.append(value)
        start = value
    correct_answer = choice(sequence)
    for index, value in enumerate(sequence):
        if value == correct_answer:
            sequence[index] = ".."
    question_user = " ".join(str(x) for x in sequence)
    return question_user, correct_answer
