import common
from common import debug
import settings

from rich import print

import itertools


def process():
    grid = []
    for l in common.read_string_file():
        grid.append([c for c in l])
    debug(grid)
    n = 0
    while True:
        if n >= len(grid[0]):
            break
        if all([row[n] == "." for row in grid]):
            # add column
            for row in grid:
                row.insert(n, ".")
            n += 1
        n += 1

    n = 0
    while True:
        if n >= len(grid):
            break
        if all([c == "." for c in grid[n]]):
            grid.insert(n, ["."] * len(grid[0]))
            n += 1
        n += 1
    debug(grid)

    d = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                d[(x, y)] = "#"

    return d


def part_1():
    d = process()
    debug(d)
    pairs = itertools.combinations(d.keys(), 2)
    dist = 0
    for (x1, y1), (x2, y2) in pairs:
        dist += abs(x2 - x1) + abs(y2 - y1)
    debug(list(pairs))
    return dist


def part_2():
    return process()
