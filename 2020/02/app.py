import re
import sys

import pyperclip

sys.path.insert(0, "../")
import common

TEST = 0
DEBUG = 0
test_data = (line for line in ("1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"))

PATTERN = re.compile("(?P<min>\d+)-(?P<max>\d+) (?P<char>.): (?P<password>.*)")

if TEST:
    input_data = test_data
else:
    input_data = common.read_string_file("input.txt")


def parse_password_line(line):
    m = re.search(PATTERN, line)
    g = m.groupdict()
    if DEBUG:
        print(g)
    return g


def check_password_line_part_1(line):
    g = parse_password_line(line)
    return int(g["min"]) <= g["password"].count(g["char"]) <= int(g["max"])


matches = 0
for (n, line) in enumerate(input_data):
    if check_password_line_part_1(line):
        matches += 1

print(matches)
