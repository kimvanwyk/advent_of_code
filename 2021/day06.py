import common
from common import debug
import settings


FIRST_DEBUG_DAYS = 18
TARGET_DAY = 80


def process():
    input_data = common.read_string_file()
    fishes = [int(i) for i in next(input_data).split(",")]
    day = 0
    while True:
        day += 1
        new_fish_count = 0
        for i in range(len(fishes)):
            fishes[i] -= 1
            if fishes[i] < 0:
                fishes[i] = 6
                new_fish_count += 1
        if new_fish_count:
            fishes.extend([8] * new_fish_count)
        if day <= FIRST_DEBUG_DAYS:
            debug(f"{day: 2}: {fishes}")
        if day == TARGET_DAY:
            return len(fishes)


def part_1():
    return process()


def part_2():
    return process()
