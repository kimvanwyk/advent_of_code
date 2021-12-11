import common
from common import debug
import settings

import numpy as np


class Grid:
    def __init__(self, input_data):
        vals = []
        for line in input_data:
            vals.append([int(l) for l in line])
        self.grid = np.array(vals, dtype=np.int8)
        (self.width, self.height) = self.grid.shape

    def flash(self, x, y):
        if self.grid[x][y] == -1:
            return
        self.grid[x][y] += 1
        if self.grid[x][y] > 9:
            self.grid[x][y] = -1
            for xd in (-1, 0, 1):
                for yd in (-1, 0, 1):
                    if (
                        (0 <= (x + xd) < self.width)
                        and (0 <= (y + yd) < self.height)
                        and not (xd == yd and xd == 0)
                    ):
                        self.flash(x + xd, y + yd)

    def step(self):
        self.steps += 1
        self.grid += 1
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] > 9:
                    self.flash(x, y)

        # all flashing done, set all -1s to 0
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] == -1:
                    self.grid[x][y] = 0
        debug(self.steps)
        debug(self.grid)

    def run_steps(self, num_steps):
        self.steps = 0
        while self.steps < num_steps:
            self.step()


def process():
    input_data = common.read_string_file()
    return Grid(input_data)


def part_1():
    grid = process()
    grid.run_steps(10)
    return ""


def part_2():
    return process()
