from rich import print

import re

import common
from common import debug
import settings

INT_NAMES = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def lookup_int_name(int_name):
    if int_name in INT_NAMES:
        return INT_NAMES[int_name]
    return int(int_name)


def process(pattern):
    debug(pattern)
    sums = []
    for line in common.read_string_file():
        groups = re.findall(pattern, line)
        debug(groups)
        sums.append(int(f"{lookup_int_name(groups[0])}{lookup_int_name(groups[-1])}"))
        debug(sums)
    return sum(sums)


def part_1():
    return process(r"\d")


def part_2():
    return process(f"\\d|{'|'.join(INT_NAMES.keys())}")
