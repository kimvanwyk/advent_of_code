import common
from common import debug
import settings

import numpy as np


def process():
    d = {}
    folds = []
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

    array = np.full((maxy, maxx), False, dtype=bool)
    for (x, y) in d.keys():
        array[y][x] = True

    for line in input_data:
        if line:
            vals = line[11:].split("=")
            folds.append((vals[0], int(vals[1])))
    return (array, folds)


def show_array(array):
    if settings.settings.debug:
        for row in array:
            debug(" ".join("#" if col else "." for col in row))


def part_1():
    (array, folds) = process()
    debug(folds)
    show_array(array)
    return ""


def part_2():
    return process()
