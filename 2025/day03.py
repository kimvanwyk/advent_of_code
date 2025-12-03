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
        for first, second in pairwise(l):
            if first > best[0]:
                best = [first, second]
            elif second > best[1]:
                best[1] = second
        debug(best)
        total += int("".join(best))
    return total


def part_2():
    return process()
