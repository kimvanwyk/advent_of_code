import common
from common import debug
import settings

from rich import print


def process():
    for line in common.read_string_file():
        yield line


def part_1():
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
    for (row, col), val in d.items():
        if type(val) is int:
            # check surrounding values
            xmin = row - 1
            xmax = row + 1
            ymin = col - 1
            ymax = col + len(str(val))
            found = False
            for x in range(xmin, xmax + 1):
                if found:
                    break
                for y in range(ymin, ymax + 1):
                    if (x, y) in d:
                        # debug(x, y, d[(x, y)])
                        if type(d[x, y]) is not int:
                            found = True
                            break
            if found:
                adjacents.append(val)
    # debug(adjacents)
    return sum(adjacents)


def part_2():
    return process()
