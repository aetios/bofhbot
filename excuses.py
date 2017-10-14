import random
import collections

with open("./excuses.txt") as file:
    excuses = [line.strip() for line in file.readlines()]
last60 = collections.deque([], 60)

def get_excuse():
    while True:
        randomnr = random.randint(0, len(excuses))
        if randomnr not in last60:
            last60.append(randomnr)
            break

    return excuses[randomnr]
