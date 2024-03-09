import common
from common import debug
import settings

import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque

from rich import print

# Heavily borrowed from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/12.py


def get_data():
    for l in common.read_string_file():
        if l:
            (pattern, combo) = l.split(" ")
            yield ([c for c in pattern], [int(c) for c in combo.split(",")])


def process_row(row):
    DP = {}

    # di == current position within dots
    # bi == current position within blocks
    # current == length of current block of '#'
    # state space is len(dots) * len(blocks) * len(dots)
    def f(dots, blocks, di, bi, current):
        key = (di, bi, current)
        if key in DP:
            return DP[key]
        if di == len(dots):
            if bi == len(blocks) and current == 0:
                return 1
            elif bi == len(blocks) - 1 and blocks[bi] == current:
                return 1
            else:
                return 0
        ans = 0
        for c in [".", "#"]:
            if dots[di] == c or dots[di] == "?":
                if c == "." and current == 0:
                    ans += f(dots, blocks, di + 1, bi, 0)
                elif (
                    c == "."
                    and current > 0
                    and bi < len(blocks)
                    and blocks[bi] == current
                ):
                    ans += f(dots, blocks, di + 1, bi + 1, 0)
                elif c == "#":
                    ans += f(dots, blocks, di + 1, bi, current + 1)
        DP[key] = ans
        return ans

    return f(row[0], row[1], 0, 0, 0)


def part_1():
    score = 0
    for row in get_data():
        debug(row)
        score += process_row(row)
    return score


def part_2():
    score = 0
    for row in get_data():
        debug(row)
        dots = "?".join(["".join(row[0])] * 5)
        blocks = row[1] * 5
        debug((dots, blocks))
        score += process_row((dots, blocks))
    return score
