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
    changed = attr.ib(default=None)
    width = attr.ib(default=0)
    height = attr.ib(default=0)
    empty_seat_threshold = attr.ib(default=4)

    def make_grid(self, input_data):
        self.grid = {}
        for (row, line) in enumerate(input_data):
            self.grid.update({((row, col), c) for (col, c) in enumerate(line)})
        self.width = len(line)
        self.height = row + 1
        self.show_grid()

    def loop_grid(self):
        for row in range(self.height):
            for col in range(self.width):
                yield (row, col, self.grid[(row, col)])

    def show_grid(self):
        out = []
        for row in range(self.height):
            out.append("  ".join(self.grid[(row, col)] for col in range(self.width)))
        debug("\n".join(out))

    def get_adjacent(self, x, y):
        adjacent = defaultdict(int)
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
            adjacent[self.grid.get((x + row, y + col), "B")] += 1
        return adjacent

    def count_types(self):
        types = defaultdict(int)
        for (row, col, val) in self.loop_grid():
            types[self.grid[(row, col)]] += 1
        return types

    def apply_occupation_rules(self):
        self.changes = []
        for (row, col, val) in self.loop_grid():
            adj = self.get_adjacent(row, col)
            if val == "L" and (adj.get("#", 0) == 0):
                self.changes.append((row, col, "#"))
            elif val == "#" and (adj.get("#", 0) >= self.empty_seat_threshold):
                self.changes.append((row, col, "L"))

        self.changed = bool(self.changes)
        for (row, col, val) in self.changes:
            self.grid[(row, col)] = val

    def apply_occupation_rules_until_stable(self):
        self.changed = True
        while self.changed:
            self.apply_occupation_rules()


def process():
    grid = Grid()
    input_data = common.read_string_file()
    grid.make_grid(input_data)
    debug(grid.show_grid())
    grid.apply_occupation_rules_until_stable()
    debug("")
    grid.show_grid()
    counts = grid.count_types()
    debug(counts)
    return counts["#"]


def part_1():
    return process()


def part_2():
    return process()
