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


def yield_free(grid):
    for current_point in grid.keys():
        if sum((grid.get(p, 0) for p in current_point.get_neighbour_points())) < 4:
            yield (current_point)


def part_1():
    grid = process()
    num_free = 0
    debug(grid)
    for point in yield_free(grid):
        num_free += 1
    return num_free


def part_2():
    grid = process()
    num_removed = 0
    while True:
        to_remove = []
        for point in yield_free(grid):
            to_remove.append(point)
        debug(to_remove, bool(to_remove))
        for point in to_remove:
            del grid[point]
        num_removed += len(to_remove)
        if not to_remove:
            break
    return num_removed
