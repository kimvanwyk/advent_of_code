from collections import Counter
import tempfile

import common
from common import debug
import settings

import numpy as np


def process():
    input_data = common.read_string_file()
    polymer = np.array([c for c in next(input_data)])
    mappings = {}
    for l in input_data:
        if l:
            mapping = l.strip().split(" -> ")
            mappings[mapping[0]] = f"{mapping[0][0]}{mapping[1]}"
    debug(polymer)
    debug(mappings)
    return (polymer, mappings)


def build_polymer(polymer, mappings, steps):
    fsource = tempfile.NamedTemporaryFile("w+", dir="files_day14", delete=False)
    fsource.write("".join(polymer))
    fsource.seek(0)
    fout = tempfile.NamedTemporaryFile("w+", dir="files_day14", delete=False)
    while True:
        res = fsource.read(2)
        if len(res) == 1:
            fout.write(res)
            break
        if not res:
            break
        debug(res)
        fout.write(mappings[res])
        fsource.seek(fsource.tell() - 1, 0)
    fout.seek(0)
    debug(fout.read())
    # for step in range(steps):
    #     for i in range(len(polymer) - 1, 0, -1):
    #         polymer = np.insert(polymer, i, mappings[f"{polymer[i-1]}{polymer[i]}"])
    #     if step < 4:
    #         debug(f"{step=}  {polymer=}")

    # count = Counter(polymer)
    # totals = count.most_common()
    # debug(f"Most common after {step+1} steps: {totals[0]}")
    # debug(f"Least common after {step+1} steps: {totals[-1]}")
    # debug(f"Difference: {totals[0][1] - totals[-1][1]}")
    # return totals[0][1] - totals[-1][1]


def part_1():
    (polymer, mappings) = process()
    build_polymer(polymer, mappings, 1)
    return ""
    # return build_polymer(polymer, mappings, 10)


def part_2():
    (polymer, mappings) = process()
    return build_polymer(polymer, mappings, 40)
