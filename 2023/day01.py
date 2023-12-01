import common
from common import debug
import settings

from rich import print


def part_1():
    sums = []
    for line in common.read_string_file():
        val = []
        for direction in (common.idempotent, reversed):
            for c in direction(line):
                if c in "0123456789":
                    val.append(c)
                    break
            debug(val)
        sums.append(int("".join(val)))
        debug(sums)
    return sum(sums)


def part_2():
    sums = []
    for line in common.read_string_file():
        val = []
        for direction in (common.idempotent, reversed):
            for c in direction(line):
                if c in "0123456789":
                    val.append(c)
                    break
            debug(val)
        sums.append(int("".join(val)))
        debug(sums)
    return sum(sums)
