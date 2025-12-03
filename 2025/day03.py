import common
from common import debug
import settings

from rich import print

from itertools import pairwise


def process():
    for l in common.read_string_file():
        yield l


def part_1():
    total = 0
    for l in process():
        best = ["0", "0"]
        for candidate in pairwise(l):
            for idx, (best_digit, candidate_digit) in enumerate(zip(best, candidate)):
                if best_digit < candidate_digit:
                    best[idx:] = candidate[idx:]
        debug(best)
        total += int("".join(best))
    return total


def part_2():
    return process()
