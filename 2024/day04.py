import common
from common import debug
import settings

from rich import print


def process(start):
    d = {}
    starts = []
    for col, l in enumerate(common.read_string_file()):
        for row, c in enumerate(l):
            d[(row, col)] = c
            if c == start:
                starts.append((row, col))
    return (d, starts)


def part_1():
    (d, starts) = process("X")
    debug(starts)
    total = 0
    for start in starts:
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
            p = (start[0], start[1])
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
