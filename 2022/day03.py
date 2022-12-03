import common
from common import debug
import settings
import string


def process():
    input_data = common.read_string_file()
    for line in input_data:
        if line:
            yield (line[: len(line) // 2], line[len(line) // 2 :])


def part_1():
    total = 0
    letters = "0" + string.ascii_letters
    for (first, second) in process():
        common = list(set(first).intersection(set(second)))
        debug(f"{set(first)}, {set(second)}, {common}, {letters.index(common[0])}")
        total += letters.index(common[0])
    return total


def part_2():
    return process()
