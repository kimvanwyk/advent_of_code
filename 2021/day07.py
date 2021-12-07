from collections import defaultdict

import common
from common import debug
import settings


# Thanks to the internet for reminding me that the sum of
# [1,2,3...n,n+1,n+2]
# for n is
# (n * (n+1)) / 2


def p1_fuel_cost(distance):
    return distance


def process(fuel_cost_func):
    input_data = common.read_string_file()
    crabs = [int(i) for i in next(input_data).split(",")]
    positions = defaultdict(int)
    for crab in crabs:
        for pos in range(min(crabs), max(crabs) + 1):
            positions[pos] += fuel_cost_func(abs(pos - crab))
    debug(positions)
    return min(positions.values())


def part_1():
    return process(p1_fuel_cost)


def part_2():
    return process()
