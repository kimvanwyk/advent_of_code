import common
from common import debug
import settings


MAPPINGS = {"forward": ("horizontal", 1), "down": ("depth", 1), "up": ("depth", -1)}


def process():
    position = {"horizontal": 0, "depth": 0}
    input_data = common.read_string_file()
    for instruction in input_data:
        (direction, amount) = instruction.split(" ")
        (key, multiplier) = MAPPINGS[direction]
        position[key] += int(amount) * multiplier
    debug(position)
    return position["horizontal"] * position["depth"]


def part_1():
    return process()


def part_2():
    return process()
