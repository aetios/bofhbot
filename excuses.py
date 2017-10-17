import random


with open("./excuses.txt") as file:
    excuses = [line.strip() for line in file.readlines()]
next_excuse_index = len(excuses)


def get_excuse():
    global next_excuse_index
    if next_excuse_index >= len(excuses):
        next_excuse_index = 0
        random.shuffle(excuses)

    next_excuse_index += 1
    return excuses[next_excuse_index-1]