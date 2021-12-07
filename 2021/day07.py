from collections import defaultdict

import common
from common import debug
import settings


def process():
    input_data = common.read_string_file()
    crabs = [int(i) for i in next(input_data).split(",")]
    positions = defaultdict(int)
    for crab in crabs:
        for pos in range(min(crabs), max(crabs) + 1):
            positions[pos] += abs(pos - crab)
    debug(positions)
    return min(positions.values())


def part_1():
    return process()


def part_2():
    return process()
