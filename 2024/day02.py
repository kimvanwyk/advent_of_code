import common
from common import debug
import settings

from rich import print

from itertools import pairwise


def process(threshold):
    total = 0
    for l in common.read_string_file():
        row = [int(c.strip()) for c in l.split(" ")]
        order = None
        fails = 0
        for pair in pairwise(row):
            if order is None:
                if pair[0] == pair[1]:
                    fails += 1
                if pair[0] > pair[1]:
                    order = (0, 1)
                else:
                    order = (1, 0)
            if not 0 < pair[order[0]] - pair[order[1]] < 4:
                fails += 1
        if fails < threshold:
            total += 1
    return total


def part_1():
    return process(1)


def part_2():
    return process()
