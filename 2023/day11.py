import common
from common import debug
import settings

from rich import print

import itertools


def process(width):
    d = {}
    for y, l in enumerate(common.read_string_file()):
        for x, c in enumerate(l):
            if c == "#":
                d[(x, y)] = "#"
    debug(d)

    max_col = len(l)
    max_row = y + 1
    debug((max_col, max_row))

    # sweep columns
    n = 0
    while True:
        if n >= max_col:
            break
        if n not in [x for (x, y) in d.keys()]:
            # new column, expand by width
            keys = list(d.keys())
            for x, y in keys:
                if x > n:
                    d[(x + width, y)] = "#"
                    del d[(x, y)]
            max_col += width
            n += width
        n += 1

    n = 0
    while True:
        if n >= max_row:
            break
        if n not in [y for (x, y) in d.keys()]:
            # new column, expand by width
            keys = list(d.keys())
            for x, y in keys:
                if y > n:
                    d[(x, y + width)] = "#"
                    del d[(x, y)]
            max_row += width
            n += width
        n += 1
    debug(d)
    debug((max_col, max_row))

    pairs = itertools.combinations(d.keys(), 2)
    dist = 0
    for (x1, y1), (x2, y2) in pairs:
        dist += abs(x2 - x1) + abs(y2 - y1)
    debug(list(pairs))
    return dist


def part_1():
    return process(1)


def part_2():
    return process(999999)
