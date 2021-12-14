from collections import Counter

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
    for step in range(10):
        for i in range(len(polymer) - 1, 0, -1):
            polymer.insert(i, mappings[f"{polymer[i-1]}{polymer[i]}"])
        if step < 4:
            debug(f"{step=}  {polymer=}")

    count = Counter(polymer)
    totals = count.most_common()
    debug(f"Most common after {step+1} steps: {totals[0]}")
    debug(f"Least common after {step+1} steps: {totals[-1]}")
    debug(f"Difference: {totals[0][1] - totals[-1][1]}")
    return totals[0][1] - totals[-1][1]


def part_2():
    return process()
