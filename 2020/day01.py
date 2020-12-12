import itertools
import math
import sys

import pyperclip

import common
import settings


def process(split, total):
    input_data = common.read_integer_file()
    for t in itertools.combinations(input_data, split):
        if sum(t) == total:
            print(t, math.prod(t))
            pyperclip.copy(math.prod(t))
            break


def part_1():
    process(2, 2020)


def part_2():
    process(3, 2020)
