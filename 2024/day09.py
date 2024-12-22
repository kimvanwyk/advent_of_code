import common
from common import debug
import settings

from rich import print


def process():
    vals = []
    for l in common.read_string_file():
        i = 0
        for n, c in enumerate(l, 1):
            if n % 2:
                # odd number, file slot
                if int(c):
                    vals.extend([i] * int(c))
            else:
                if int(c):
                    vals.extend(["."] * int(c))
                i += 1
    return vals


def part_1():
    vals = process()
    debug(f"{vals=}")
    while True:
        if not "." in vals:
            break
        i = vals.index(".")
        v = vals.pop(-1)
        vals[i] = v
        while vals[-1] == ".":
            del vals[-1]
        debug(vals)
    checksum = 0
    for n, v in enumerate(vals):
        if v != ".":
            checksum += n * v
    return checksum


def part_2():
    return process()
