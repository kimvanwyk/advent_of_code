import common
from common import debug
import settings

import attr


@attr.define
class Instruction:
    x_range: tuple
    y_range: tuple
    z_range: tuple
    position: bool


def process():
    input_data = common.read_string_file()

    for l in input_data:
        (position, range_strings) = l.split(" ")
        ranges = []
        for range_string in range_strings.split(","):
            ranges.append(tuple([int(i) for i in range_string[2:].split("..")]))
        yield Instruction(*ranges, position == "on")


def part_1():
    for instruction in process():
        debug(instruction)
    return ""


def part_2():
    return process()
