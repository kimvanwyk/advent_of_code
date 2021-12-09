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

    def show_grid(self):
        if settings.settings.debug:
            for y in range(self.height):
                print("".join(str(self.grid[(x, y)]) for x in range(self.width)))

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


def process():
    input_data = common.read_string_file()
    grid = Grid()
    for line in input_data:
        grid.add_row(int(c) for c in line)
    grid.show_grid()
    return grid.process_low_points()


def part_1():
    return process()


def part_2():
    return process()
