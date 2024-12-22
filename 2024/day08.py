import common
from common import debug, Point
import settings

from rich import print

from collections import defaultdict


def process():
    nodes = defaultdict(list)
    y = 0
    for l in common.read_string_file():
        if l:
            y += 1
            for x, c in enumerate(l, 1):
                if c != ".":
                    nodes[c].append(Point(x, y))
    return (nodes, Point(1, 1), Point(x, y))


def part_1():
    (nodes, min_point, max_point) = process()
    # nodes = {"a": [Point(5, 4), Point(6, 6)]}
    # nodes = {"a": [Point(5, 4), Point(6, 6), Point(9, 5)]}
    # min_point = Point(1, 1)
    # max_point = Point(10, 10)
    antinodes = {}
    for frequency, points in nodes.items():
        for anchor in points:
            for point in points:
                if anchor != point:
                    diff = anchor - point
                    debug(f"{diff=}")
                    debug(f"{(anchor, point)=}")
                    p = anchor + diff
                    if p.in_bounds(min_point, max_point):
                        antinodes[p] = 1
    debug(f"{antinodes=}")
    return len(antinodes)


def part_2():
    return process()
