import common
from common import debug
import settings

from rich import print

from collections import defaultdict


def process():
    d = {}
    row = -1
    coord = None
    int_origins = defaultdict(list)
    for line in common.read_string_file():
        row += 1
        in_num = False
        coord = None
        for col, c in enumerate(line):
            if c in "0123456789":
                if not in_num:
                    coord = (col, row)
                    in_num = True
                int_origins[coord].append(c)
            else:
                in_num = False
                if c != ".":
                    d[(col, row)] = c

    for (col, row), val in int_origins.items():
        s = "".join(val)
        i = int(s)
        for x in range(col, col + len(s)):
            d[(x, row)] = i
        int_origins[(col, row)] = i
    debug(int_origins)
    debug(d)
    return (int_origins, d)


def part_1():
    (int_origins, d) = process()
    adjacents = []
    for (col, row), val in int_origins.items():
        # check surrounding values
        xmin = col - 1
        xmax = col + len(str(val))
        ymin = row - 1
        ymax = row + 1
        found = False
        for y in range(ymin, ymax + 1):
            if found:
                break
            for x in range(xmin, xmax + 1):
                # debug((x, y, d.get((x, y))))
                if (x, y) in d:
                    if type(d[x, y]) is not int:
                        found = True
                        break
        if found:
            adjacents.append(val)
    # debug(adjacents)
    return sum(adjacents)


def part_2():
    d = {}
    row = -1
    coord = None
    for line in process():
        row += 1
        in_num = False
        if coord:
            d[coord] = int("".join(d[coord]))
            coord = None
            in_num = False
        for col, c in enumerate(line):
            if c in "0123456789":
                if not in_num:
                    coord = (row, col)
                    in_num = True
                    d[coord] = [c]
                else:
                    d[coord].append(c)
            else:
                if coord:
                    d[coord] = int("".join(d[coord]))
                    coord = None
                in_num = False
                if c != ".":
                    d[(row, col)] = c
    debug(d)
    adjacents = []
