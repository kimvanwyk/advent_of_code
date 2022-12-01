import common
from common import debug
import settings


def process():
    input_data = common.read_string_file()
    entries = []
    sum = 0
    for line in input_data:
        if line == "":
            entries.append(sum)
            sum = 0
        else:
            sum += int(line)
    return entries


def part_1():
    entries = process()
    return max(entries)


def part_2():
    return process()
