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
    total = 0
    letters = "0" + string.ascii_letters
    groups = []
    for (n, line) in enumerate(process(), 1):
        debug(f"{n=} {n % 3=}")
        groups.append(set([c for c in line]))
        if not n % 3:
            debug(groups)
            # clever intersection trick from https://blog.finxter.com/how-to-intersect-multiple-sets-in-python/
            common = list(groups.pop().intersection(*groups))[0]
            debug(f"{common=}")
            total += letters.index(common)
            groups = []
    return total
