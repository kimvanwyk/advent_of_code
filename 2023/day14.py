import common
from common import debug
import settings

from rich import print


def print_grid(d):
    max_col = max([k[0] for k in d if k[1] == 1])
    max_row = max([k[1] for k in d if k[0] == 1])
    for row in range(1, max_row + 1):
        out = []
        for col in range(1, max_col + 1):
            out.append(d[(col, row)])
        debug("".join(out))


def tilt_north(d, max_col, max_row):
    od = {}
    for col in range(1, max_col + 1):
        l = "".join([d[(col, r)] for r in range(1, max_row + 1)])
        # debug(l)
        sections = []
        for section in l.split("#"):
            s = [c for c in section]
            s.sort(reverse=True)
            sections.append("".join(s))
        sorted = "#".join(sections)
        for r, c in enumerate(sorted, 1):
            od[(col, r)] = c
    print_grid(od)
    return od


def get_load(d):
    max_col = max([k[0] for k in d if k[1] == 1])
    max_row = max([k[1] for k in d if k[0] == 1])
    load = 0
    for row in range(1, max_row + 1):
        multiplier = max_row + 1 - row
        load += (
            len(
                [d[(col, row)] for col in range(1, max_col + 1) if d[(col, row)] == "O"]
            )
            * multiplier
        )
    return load


def process():
    d = {}
    row = 1
    for l in common.read_string_file():
        if l:
            for col, c in enumerate(l, 1):
                d[(col, row)] = c
            row += 1
    print_grid(d)
    return d


def part_1():
    d = process()
    max_col = max([k[0] for k in d if k[1] == 1])
    max_row = max([k[1] for k in d if k[0] == 1])
    debug("")
    od = tilt_north(d, max_col, max_row)
    return get_load(od)


def part_2():
    return process()
