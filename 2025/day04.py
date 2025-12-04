import common
from common import debug, Point
import settings

from rich import print


def process():
    grid = {}
    y = -1
    for l in common.read_string_file():
        y += 1
        for x, c in enumerate(l):
            if c == "@":
                grid[Point(x, y)] = 1
    return grid


def part_1():
    grid = process()
    num_free = 0
    debug(grid)
    for current_point in grid.keys():
        if sum((grid.get(p, 0) for p in current_point.get_neighbour_points())) < 4:
            num_free += 1
    return num_free


def part_2():
    return process()
