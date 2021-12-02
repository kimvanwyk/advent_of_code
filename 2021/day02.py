import common
from common import debug
import settings


MAPPINGS = {"down": 1, "up": -1}


def process():
    horizontal = 0
    depth = 0
    aim = 0
    input_data = common.read_string_file()
    for instruction in input_data:
        (direction, amount) = instruction.split(" ")
        if direction in MAPPINGS:
            aim += int(amount) * MAPPINGS[direction]
        else:
            # direction must be forward
            horizontal += int(amount)
            depth += aim * int(amount)
    debug(locals())
    return horizontal * depth


def part_1():
    return process()


def part_2():
    return process()
