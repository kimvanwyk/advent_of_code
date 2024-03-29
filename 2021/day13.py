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
        for row in self.array:
            print(" ".join("#" if col else "." for col in row))

    def fold(self, fold):
        pivot = fold[1]
        if fold[0] == "y":
            axis = 0
            rev = False
            edge = self.array.shape[0] - 1
        else:
            axis = 1
            rev = True
            edge = self.array.shape[1] - 1
        for diff in range(abs(edge - pivot), 0, -1):
            target_idx = [slice(pivot - diff, pivot - diff + 1), slice(None)]
            source_idx = [slice(pivot + diff, pivot + diff + 1), slice(None)]
            if rev:
                target_idx.reverse()
                source_idx.reverse()
            target_idx = tuple(target_idx)
            source_idx = tuple(source_idx)
            self.array[target_idx] = self.array[target_idx] | self.array[source_idx]
            self.array = np.delete(self.array, pivot + diff, axis)
        self.array = np.delete(self.array, pivot, axis)
        return np.count_nonzero(self.array == True)

    def apply_folds(self, limit=None):
        for (n, fold) in enumerate(self.folds, 1):
            val = self.fold(fold)
            if settings.settings.debug:
                self.show()
            debug(val)
            debug("")
            if limit and (n == limit):
                return val
        return val


def part_1():
    a = Array()
    return a.apply_folds(1)


def part_2():
    a = Array()
    a.apply_folds()
    a.show()
    return ""
