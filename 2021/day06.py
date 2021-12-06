import common
from common import debug
import settings

import numpy as np


FIRST_DEBUG_DAYS = 18


def process(target_day):
    input_data = common.read_string_file()
    fishes = np.array([int(i) for i in next(input_data).split(",")], dtype=np.int8)
    day = 0
    debug(fishes)
    while True:
        day += 1
        fishes -= 1
        new_fish_count = (fishes == -1).sum()
        fishes[fishes == -1] = 6
        if new_fish_count:
            fishes = np.append(fishes, [8] * new_fish_count)
        if day <= FIRST_DEBUG_DAYS:
            debug(f"{day: 2}: {fishes}")
        if day == target_day:
            return len(fishes)


def part_1():
    return process(18 if settings.settings.test else 80)


def part_2():
    return process(256)
