import common
from common import debug
import settings

from rich import print

import operator


def process():
    for l in common.read_string_file():
        yield (l[0], int(l[1:]))
    return ""


def part_1():
    zeroes = 0
    position = 50
    for direction, values in process():
        values = values % 100
        op = operator.add if direction == "R" else operator.sub
        position = op(position, values)
        if position < 0:
            position = 100 + position
        elif position > 99:
            position = position - 100
        if position == 0:
            zeroes += 1
        debug((direction, values, position, zeroes))
    return zeroes


def part_2():
    zeroes = 0
    end_pos = 50
    for direction, values in process():
        start_pos = end_pos
        zeroes += values // 100
        values = values % 100
        op = operator.add if direction == "R" else operator.sub
        end_pos = op(start_pos, values)
        if end_pos == 100:
            end_pos = 0
        if end_pos == 0:
            zeroes += 1
        if end_pos < 0:
            end_pos = 100 + end_pos
            if start_pos > 0:
                zeroes += 1
        elif end_pos > 100:
            end_pos = end_pos - 100
            if start_pos > 0:
                zeroes += 1
        debug((direction, values, end_pos, zeroes))
    return zeroes
