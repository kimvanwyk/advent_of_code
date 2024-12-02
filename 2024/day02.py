import common
from common import debug
import settings

from rich import print

from itertools import pairwise


def process():
    for l in common.read_string_file():
        yield [int(c.strip()) for c in l.split(" ")]


def part_1():
    total = 0
    for row in process():
        order = None
        success = True
        for pair in pairwise(row):
            if order is None:
                if pair[0] == pair[1]:
                    success = False
                    break
                if pair[0] > pair[1]:
                    order = (0, 1)
                else:
                    order = (1, 0)
            if not 0 < pair[order[0]] - pair[order[1]] < 4:
                success = False
                break
        if success:
            total += 1
    return total


def part_2():
    return process()
