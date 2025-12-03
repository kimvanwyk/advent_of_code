import common
from common import debug
import settings

from rich import print


def process():
    for l in common.read_string_file():
        yield l


def part_1():
    total = 0
    for l in process():
        first_highest = "0"
        second_highest = "0"
        first_idx = 0
        second_idx = 0
        for i, c in enumerate(l[:-1], 0):
            if c > first_highest:
                first_highest = c
                first_idx = i
        for i, c in enumerate(l[(first_idx + 1) :], first_idx + 1):
            if c > second_highest:
                second_highest = c
                second_idx = i
        debug(first_idx, second_idx, f"{l[first_idx]}{l[second_idx]}")
        total += int(f"{l[first_idx]}{l[second_idx]}")
    return total


def part_2():
    return process()
