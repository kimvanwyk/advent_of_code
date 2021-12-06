import common
from common import debug
import settings

from collections import defaultdict

FIRST_DEBUG_DAYS = 18


def process(target_day):
    input_data = common.read_string_file()
    fishes = defaultdict(int)
    for fish in [int(i) for i in next(input_data).split(",")]:
        fishes[fish] += 1
    day = 0
    debug(fishes)
    while True:
        day += 1
        new = fishes[0]
        for n in range(1, 9):
            fishes[n - 1] = fishes[n]
        fishes[6] += new
        fishes[8] = new
        if day <= FIRST_DEBUG_DAYS:
            debug(f"{day: 2}: {fishes}  {new=}")
        if day == target_day:
            debug(list(fishes.values()))
            return sum(list(fishes.values()))


def part_1():
    return process(18 if settings.settings.test else 80)


def part_2():
    return process(256)
