import common
from common import debug
import settings

import numpy as np


def process():
    input_data = common.read_string_file()
    array = np.array([[int(c) for c in line] for line in input_data], dtype=np.uint8)
    debug(array)
    return array


def part_1():
    array = process()
    visible = 2 * array.shape[0] + 2 * (array.shape[1] - 2)
    for ((row, col), tree) in np.ndenumerate(array):
        if 0 < row < array.shape[0] - 1 and 0 < col < array.shape[1] - 1:
            for (name, ri, ci) in (
                ("top", slice(None, row), col),
                ("bottom", slice(row + 1, None), col),
                ("left", row, slice(None, col)),
                ("right", row, slice(col + 1, None)),
            ):
                debug(
                    f"{name=}, {array[ri, ci]=}, {tree=}, {max(array[ri, ci]) < tree=}"
                )
                if max(array[ri, ci]) < tree:
                    visible += 1
                    # only care about any single visibility
                    break
            debug("")
    return visible


def part_2():
    array = process()
    best_site = 0
    for ((row, col), tree) in np.ndenumerate(array):
        score = 1
        if 0 < row < array.shape[0] - 1 and 0 < col < array.shape[1] - 1:
            for (name, ri, ci, flip) in (
                ("top", slice(None, row), col, np.flip),
                ("bottom", slice(row + 1, None), col, lambda x: x),
                ("left", row, slice(None, col), np.flip),
                ("right", row, slice(col + 1, None), lambda x: x),
            ):
                debug(f"{name=}, {flip(array[ri, ci])=}, {tree=}")
                for (n, height) in enumerate(flip(array[ri, ci]), 1):
                    debug(f"{n=} {height=}")
                    if height >= tree:
                        break
                score *= n
                debug(f"{score=}")
            debug("")
        if score > best_site:
            best_site = score
    return best_site
