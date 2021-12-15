from collections import Counter
import math

import common
from common import debug
import settings

import numpy as np


def process():
    input_data = common.read_string_file()
    line = next(input_data)
    pairs = Counter()
    for i in range(len(line) - 1):
        pairs[f"{line[i]}{line[i+1]}"] += 1
    mappings = {}
    for l in input_data:
        if l:
            mapping = l.strip().split(" -> ")
            mappings[mapping[0]] = (
                f"{mapping[0][0]}{mapping[1]}",
                f"{mapping[1]}{mapping[0][1]}",
            )
    debug(pairs)
    debug(mappings)
    return (pairs, mappings)


def build_pairs(pairs, mappings, steps):
    for step in range(steps):
        new_pairs = Counter()
        for pair in pairs:
            for p in mappings[pair]:
                new_pairs[p] += pairs[pair]
        pairs = new_pairs
        if step < 4:
            debug(step + 1)
            debug(pairs)

    count = Counter()
    for (k, v) in pairs.items():
        for c in k:
            count[c] += v
    for (k, v) in count.items():
        count[k] = math.ceil(v / 2)

    totals = count.most_common()
    debug(f"Most common after {step+1} steps: {totals[0]}")
    debug(f"Least common after {step+1} steps: {totals[-1]}")
    debug(f"Difference: {totals[0][1] - totals[-1][1]}")
    return totals[0][1] - totals[-1][1]


def part_1():
    (pairs, mappings) = process()
    return build_pairs(pairs, mappings, 10)


def part_2():
    (polymer, mappings) = process()
    return build_polymer(polymer, mappings, 40)
