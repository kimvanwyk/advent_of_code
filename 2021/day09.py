from collections import Counter
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

    def process_basins(self):
        basin_val = 0
        for y in range(self.height):
            for x in range(self.width):
                if 0 <= self.grid[(x, y)] < 9:
                    # check if the four points nearby are part of a basin
                    for pos in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                        neighbour = self.grid.get(pos, 10)
                        if neighbour < 0:
                            self.grid[(x, y)] = neighbour
                            break
                    else:
                        # new basin
                        basin_val -= 1
                        self.grid[(x, y)] = basin_val

                if self.grid[(x, y)] < 0:
                    # already in a basin, mark neighbours
                    for pos in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                        if self.grid.get(pos, None) and 0 <= self.grid[pos] < 9:
                            self.grid[pos] = self.grid[(x, y)]

        self.show_grid()

        sizes = Counter(v for v in self.grid.values() if v < 0)
        print(sizes.most_common(3))
        return prod(v[1] for v in sizes.most_common(3))


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
