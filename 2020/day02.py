import re
import sys

import pyperclip

import common
from common import debug
import settings

PATTERN = re.compile("(?P<pos1>\d+)-(?P<pos2>\d+) (?P<char>.): (?P<password>.*)")


def parse_password_line(line):
    m = re.search(PATTERN, line)
    g = m.groupdict()
    debug(g)
    return g


def check_password_line_part_1(line):
    g = parse_password_line(line)
    return int(g["pos1"]) <= g["password"].count(g["char"]) <= int(g["pos2"])


def check_password_line_part_2(line):
    g = parse_password_line(line)
    return (g["password"][int(g["pos1"]) - 1] == g["char"]) ^ (
        g["password"][int(g["pos2"]) - 1] == g["char"]
    )


def process(check):

    matches = 0
    input_data = common.read_string_file()
    for (n, line) in enumerate(input_data):
        c = check(line)
        debug((n, c))
        if c:
            matches += 1
    return matches


def part_1():
    return process(check_password_line_part_1)


def part_2():
    return process(check_password_line_part_2)
