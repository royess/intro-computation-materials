# a debugging example
import random


def print_random():
    print('hello', end=' ')
    print(random.randint(0, 10))


for i in range(10):
    print_random()
