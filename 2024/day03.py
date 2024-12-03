import common
from common import debug
import settings

from rich import print

import re

PATTERN = re.compile("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")


def process():
    return common.read_string_file()


def check_lines(lines):
    total = 0
    for line in lines:
        debug(line)
        for match in PATTERN.finditer(line):
            if "mul" in match.group():
                (left, right) = (int(i) for i in match.group()[4:-1].split(","))
                debug(left, right)
                total += left * right
    return total


def part_1():
    return check_lines(process())


def part_2():
    return process()
