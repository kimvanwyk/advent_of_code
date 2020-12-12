import itertools
import math
import sys

import pyperclip

import common
import settings


def process(split, total):
    if settings.TEST:
        input_file = "day01_test_input.txt"
    else:
        input_file = "day01_input.txt"
    input_data = common.read_integer_file(input_file)
    for t in itertools.combinations(input_data, split):
        if sum(t) == total:
            print(t, math.prod(t))
            pyperclip.copy(math.prod(t))
            break


def part_1():
    process(2, 2020)


def part_2():
    process(3, 2020)


settings.TEST = 0
part_1()
part_2()
