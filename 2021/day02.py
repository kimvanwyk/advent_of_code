import common
from common import debug
import settings


def process_p1():
    mappings = {"forward": ("horizontal", 1), "down": ("depth", 1), "up": ("depth", -1)}
    position = {"horizontal": 0, "depth": 0}
    input_data = common.read_string_file()
    for instruction in input_data:
        (direction, amount) = instruction.split(" ")
        (key, multiplier) = mappings[direction]
        position[key] += int(amount) * multiplier
    debug(position)
    return position["horizontal"] * position["depth"]


def process_p2():
    mappings = {"down": 1, "up": -1}
    horizontal = 0
    depth = 0
    aim = 0
    input_data = common.read_string_file()
    for instruction in input_data:
        (direction, amount) = instruction.split(" ")
        if direction in mappings:
            aim += int(amount) * mappings[direction]
        else:
            # direction must be forward
            horizontal += int(amount)
            depth += aim * int(amount)
    debug(locals())
    return horizontal * depth


def part_1():
    return process_p1()


def part_2():
    return process_p2()
