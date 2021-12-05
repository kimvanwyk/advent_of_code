from collections import defaultdict

import common
from common import debug
import settings


def print_grid(grid):
    if settings.settings.debug:
        maxx = max([p[0] for p in grid.keys()]) + 1
        maxy = max([p[1] for p in grid.keys()]) + 1
        for x in range(maxx):
            for y in range(maxy):
                # print(row, col, grid[(row, col)])
                val = grid[(y, x)] or "."
                print(f"{val}  ", end="")
            print()


def process():

    input_data = common.read_string_file()
    grid = defaultdict(int)
    for line in input_data:
        # debug(line)
        if line:
            points = [
                [int(p) for p in point.strip().split(",")] for point in line.split("->")
            ]
            for (fixed_pos, var_pos) in ((0, 1), (1, 0)):
                increment = [None, None]
                straight = False
                if points[0][fixed_pos] == points[1][fixed_pos]:
                    straight = True
                    difference = points[1][var_pos] - points[0][var_pos]
                    increment[fixed_pos] = 0
                    increment[var_pos] = difference // abs(difference)
                    debug(f"{points=}  {increment=}")
                    point = points[0]
                    while True:
                        grid[tuple(point)] += 1
                        debug(tuple(point))
                        point[0] += increment[0]
                        point[1] += increment[1]
                        if point == points[1]:
                            grid[tuple(point)] += 1
                            debug(tuple(point))
                            break
                if straight:
                    break
    debug(grid)
    print_grid(grid)
    return len([v for v in grid.values() if v >= 2])


def part_1():
    return process()


def part_2():
    return process()
