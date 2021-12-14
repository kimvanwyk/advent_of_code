import common
from common import debug
import settings


def process():
    input_data = common.read_string_file()
    polymer = [c for c in next(input_data)]
    mappings = dict([(l.strip().split(" -> ")) for l in input_data if l])
    debug(polymer)
    debug(mappings)
    return (polymer, mappings)


def part_1():
    (polymer, mappings) = process()
    return ""


def part_2():
    return process()
