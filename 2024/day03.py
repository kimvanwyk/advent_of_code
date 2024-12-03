import common
from common import debug
import settings

# from rich import print

import re

PATTERN = re.compile("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")


def process():
    return common.read_string_file()


def check_lines(lines):
    total = 0
    process = True
    for line in lines:
        for match in PATTERN.finditer(line):
            m = match.group()
            debug(m)
            if process and ("mul" in m):
                (left, right) = (int(i) for i in m[4:-1].split(","))
                # debug(left, right)
                total += left * right
            elif "do()" in m:
                # debug("do")
                process = True
            elif "don't()" in m:
                # debug("don't")
                process = False
    return total


def part_1():
    return check_lines(process())


def part_2():
    return check_lines(process())
