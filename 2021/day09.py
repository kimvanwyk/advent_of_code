from collections import Counter, defaultdict
from math import prod

import common
from common import debug
import settings


class Grid:
    def __init__(self):
        self.width = None
        self.height = 0
        self.grid = {}

    def add_row(self, vals):
        for (x, val) in enumerate(vals):
            self.grid[(x, self.height)] = val
        if self.width is None:
            self.width = x + 1
        self.height += 1

    def show_grid(self, spacer=""):
        if settings.settings.debug:
            for y in range(self.height):
                print("".join(f"{self.grid[(x, y)]: 4}" for x in range(self.width)))
            print()

    def process_low_points(self):
        self.risk = 0
        for y in range(self.height):
            for x in range(self.width):
                val = self.grid[(x, y)]
                if val < 9 and all(
                    val < self.grid.get((x + xd, y + yd), 10)
                    for (xd, yd) in ((-1, 0), (1, 0), (0, -1), (0, 1))
                ):
                    debug(f"Low point found at {(x,y)}: {val}")
                    self.risk += 1 + val
        return self.risk

    def point_in_basin(self, x, y):
        # if the point has any higher neighbours, add to the basin and expand outwards
        # print(x, y, self.basins)
        val = self.grid.get((x, y), 10)
        if val >= 9:
            return False
        if any(
            self.grid[(x, y)] <= self.grid.get(pos, 10)
            for pos in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1))
        ):
            self.grid[(x, y)] = 10
            self.basins[self.basin_val] += 1
            for (nx, ny) in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                self.point_in_basin(nx, ny)

    def process_basins(self):
        self.basin_val = 0
        self.basins = defaultdict(int)
        for y in range(self.height):
            for x in range(self.width):
                val = self.grid[(x, y)]
                if val < 9 and all(
                    val < self.grid.get((x + xd, y + yd), 10)
                    for (xd, yd) in ((-1, 0), (1, 0), (0, -1), (0, 1))
                ):
                    # found a low point, work in all directions from it until the point doesn't have any higher neighbours or is 9
                    self.basin_val += 1
                    self.point_in_basin(x, y)

        self.show_grid()

        sizes = list(self.basins.values())
        sizes.sort(reverse=True)
        debug(sizes)
        return prod(sizes[:3])


def process():
    input_data = common.read_string_file()
    grid = Grid()
    for line in input_data:
        grid.add_row(int(c) for c in line)
    grid.show_grid()
    return grid


def part_1():
    grid = process()
    return grid.process_low_points()


def part_2():
    grid = process()
    return grid.process_basins()
