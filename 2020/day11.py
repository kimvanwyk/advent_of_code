from collections import defaultdict

import attr

import common
from common import debug
import settings


@attr.s
class Grid:

    grid = attr.ib(default=attr.Factory(list))
    current_idx = attr.ib(default=(1, 1))
    current_val = attr.ib(default=None)
    adjacent = attr.ib(default=None)

    def make_grid(self, input_data):
        self.grid = []
        for line in input_data:
            self.grid.append(["."])
            self.grid[-1].extend([c for c in line])
            self.grid[-1].append(".")
        self.grid.insert(0, ["."] * len(self.grid[-1]))
        self.grid.append(["."] * len(self.grid[-1]))
        self.set_adjacent()

    def show_grid(self):
        debug([line[1:-1] for line in self.grid[1:-1]], pretty=True)

    def set_current_idx(self, x, y):
        self.current_idx = (x, y)
        self.current_val = self.grid[x][y]
        self.set_adjacent()

    def update_val(self, val):
        (x, y) = self.current_idx
        self.grid[x][y] = val
        self.current_val = val

    def set_adjacent(self):
        self.adjacent = defaultdict(int)
        for (row, col) in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ):
            (cx, cy) = self.current_idx
            self.adjacent[self.grid[cx + row][cy + col]] += 1

    def apply_occupation_rules(self):
        top = self.grid[0][:]
        self.new_grid = [top]
        for row in range(1, len(self.grid) - 1):
            self.new_grid.append(["."])
            for col in range(1, len(self.grid[0]) - 1):
                self.set_current_idx(row, col)
                # print(
                #     self.current_val,
                #     self.adjacent,
                # )
                if self.current_val == "L" and (self.adjacent.get("#", 0) == 0):
                    # print(f"update [{row}][{col}] from L to #")
                    self.new_grid[-1].append("#")
                elif self.current_val == "#" and (self.adjacent.get("#", 0) >= 4):
                    # print(f"update [{row}][{col}] from # to L")
                    self.new_grid[-1].append("L")
                else:
                    self.new_grid[-1].append(self.current_val)
            self.new_grid[-1].append(".")
        self.new_grid.append(top)

        self.grid = self.new_grid


def process():
    grid = Grid()
    input_data = common.read_string_file()
    grid.make_grid(input_data)
    grid.show_grid()
    print()
    grid.apply_occupation_rules()
    grid.show_grid()
    print()
    grid.apply_occupation_rules()
    grid.show_grid()
    return ""


def part_1():
    return process()


def part_2():
    return process()
