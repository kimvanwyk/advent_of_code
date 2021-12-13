import common
from common import debug
import settings

import numpy as np


class Array:
    def __init__(self):
        d = {}
        self.folds = []
        input_data = common.read_string_file()
        maxx = 0
        maxy = 0
        for line in input_data:
            if not line.strip():
                break
            (x, y) = [int(l) for l in line.strip().split(",")]
            d[(x, y)] = 1
            if x >= maxx:
                maxx = x + 1
            if y >= maxy:
                maxy = y + 1

        self.array = np.full((maxy, maxx), False, dtype=bool)
        for (x, y) in d.keys():
            self.array[y][x] = True

        for line in input_data:
            if line:
                vals = line[11:].split("=")
                self.folds.append((vals[0], int(vals[1])))

    def show(self):
        if settings.settings.debug:
            for row in self.array:
                debug(" ".join("#" if col else "." for col in row))

    # def fold(self, fold):


def part_1():
    a = Array()
    debug(a.folds)
    a.show()
    return ""


def part_2():
    return process()
