import common
from common import debug
import settings
import string


def process():
    input_data = common.read_string_file()
    return input_data


def part_1():
    total = 0
    letters = "0" + string.ascii_letters
    for line in process():
        if line:
            (first, second) = (line[: len(line) // 2], line[len(line) // 2 :])
        common = list(set(first).intersection(set(second)))
        debug(f"{set(first)}, {set(second)}, {common}, {letters.index(common[0])}")
        total += letters.index(common[0])
    return total


def part_2():
    return process()
