import common
from common import debug, Point
import settings

from rich import print

from collections import defaultdict

DIRECTION = {"<": Point(-1, 0), "^": Point(0, -1), ">": Point(1, 0), "v": Point(0, 1)}
TURN = {"^": ">", ">": "v", "v": "<", "<": "^"}


def process():
    d = {}
    for y, l in enumerate(common.read_string_file()):
        for x, c in enumerate(l):
            d[Point(x, y)] = c
            if c in "<>^v":
                start = Point(x, y)
    return (d, start)


def part_1():
    (d, start) = process()
    debug(start)
    direction = d[start]
    debug(direction)
    p = start
    # Replace start position so later re-treads treat it as empty
    d[p] = "."
    steps = defaultdict(int)
    steps[p] += 1
    while True:
        new_p = p + DIRECTION[direction]
        if new_p not in d:
            break
        elif d[new_p] == "#":
            direction = TURN[direction]
        elif d[new_p] == ".":
            p = new_p
            steps[p] += 1
        debug((p, new_p, direction, len(steps)))
    return len(steps)


def part_2():
    return process()
