import common
from common import debug
import settings

from rich import print


def process():
    d = {}
    xes = []
    for col, l in enumerate(common.read_string_file()):
        for row, c in enumerate(l):
            d[(row, col)] = c
            if c == "X":
                xes.append((row, col))
    return (d, xes)


def part_1():
    (d, xes) = process()
    debug(xes)
    total = 0
    for x in xes:
        for direction in (
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
        ):
            p = (x[0], x[1])
            success = True
            for letter in "MAS":
                p = (p[0] + direction[0], p[1] + direction[1])
                # debug(p, letter)
                if d.get(p, None) != letter:
                    success = False
                    break
            if success:
                total += 1
    return total


def part_2():
    return process()
