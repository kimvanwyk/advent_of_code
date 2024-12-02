import common
from common import debug
import settings

from rich import print

from itertools import pairwise


def process():
    for l in common.read_string_file():
        yield [int(c.strip()) for c in l.split(" ")]


def check_row(row, threshold):
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
    return fails < threshold


def part_1():
    total = 0
    for row in process():
        if check_row(row, 1):
            total += 1
    return total


def part_2():
    total = 0
    for row in process():
        success = False
        debug(row)
        success = check_row(row, 1)
        if success:
            total += 1
        else:
            for n in range(len(row)):
                r = row[:n] + row[n + 1 :]
                debug(r)
                success = check_row(r, 1)
                if success:
                    break
            if success:
                total += 1
    return total
