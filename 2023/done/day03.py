import common
from common import debug
import settings

from attrs import define
from rich import print

from collections import defaultdict


@define
class Val:
    val: int = 0

    def __add__(self, a):
        return self.val + a.val


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
        i = Val(int(s))
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
        xmax = col + len(str(val.val))
        ymin = row - 1
        ymax = row + 1
        found = False
        for y in range(ymin, ymax + 1):
            if found:
                break
            for x in range(xmin, xmax + 1):
                if (x, y) in d:
                    # if type(d[x, y]) is not type(Val()):
                    if not isinstance(d[x, y], type(Val())):
                        found = True
                        break
        if found:
            adjacents.append(val)
    debug(adjacents)
    return sum([a.val for a in adjacents])


def part_2():
    (int_origins, d) = process()
    debug(d)
    gear_sum = 0
    for (col, row), val in d.items():
        if val == "*":
            adjacents = defaultdict(list)
            brk = False
            debug((col, row, val))
            for y in range(row - 1, row + 2):
                if brk:
                    break
                for x in range(col - 1, col + 2):
                    if ((x, y) in d) and isinstance(d[x, y], type(Val())):
                        adjacents[id(d[x, y])] = d[x, y]
                        if len(adjacents) > 2:
                            brk = True
                            break
            debug((brk, adjacents))
            if len(adjacents) == 2:
                debug((x, y, adjacents))
                vals = [v.val for v in adjacents.values()]
                debug(vals)
                gear_sum += vals[0] * vals[1]
    return gear_sum
