import itertools
import math
import sys

import pyperclip

import common
from common import debug


def process(split, total):
    input_data = common.read_integer_file()
    for t in itertools.combinations(input_data, split):
        if sum(t) == total:
            debug((t, math.prod(t)))
            return math.prod(t)


def part_1():
    return process(2, 2020)


def part_2():
    return process(3, 2020)
