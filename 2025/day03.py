import common
from common import debug
import settings

from rich import print

from collections import deque
from itertools import islice


def process():
    for l in common.read_string_file():
        yield l


# https://mathspp.com/blog/generalising-itertools-pairwise#using-deque
def nwise(iterable, n):
    iterable = iter(iterable)
    window = deque(islice(iterable, n - 1), maxlen=n)
    for value in iterable:
        window.append(value)
        yield tuple(window)


def part_1():
    total = 0
    for l in process():
        best = ["0", "0"]
        # Inspired by Rodrigo's solution
        # loop over pairs and check each digit. If a digit is higher, all the subsequent
        # digits must be better too as the first digit is higher
        for candidate in nwise(l, 2):
            for idx, (best_digit, candidate_digit) in enumerate(zip(best, candidate)):
                if best_digit < candidate_digit:
                    best[idx:] = candidate[idx:]
        debug(best)
        total += int("".join(best))
    return total


def part_2():
    return process()
