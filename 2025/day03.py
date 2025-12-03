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


def process_bank(bank, num_batteries):
    best = ["0"] * num_batteries
    # Inspired by Rodrigo's solution
    # loop over pairs and check each digit. If a digit is higher, all the subsequent
    # digits must be better too as the first digit is higher
    for candidate in nwise(bank, num_batteries):
        for idx, (best_digit, candidate_digit) in enumerate(zip(best, candidate)):
            if best_digit < candidate_digit:
                best[idx:] = candidate[idx:]
    debug(best)
    return int("".join(best))


def part_1():
    total = 0
    for l in process():
        total += process_bank(l, 2)
    return total


def part_2():
    total = 0
    for l in process():
        total += process_bank(l, 12)
    return total
