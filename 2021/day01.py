import common
from common import debug
import settings


def process():
    inc = 0
    input_data = common.read_integer_file()
    first = next(input_data)
    for second in input_data:
        debug(f"{first=} {second=}")
        if second > first:
            inc += 1
        first = second
    return inc


def part_1():
    return process()


def part_2():
    return process()
