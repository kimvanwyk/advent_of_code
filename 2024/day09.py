import common
from common import debug
import settings

from rich import print


def process():
    files = {}
    frees = {}
    for line in common.read_string_file():
        i = 0
        j = 0
        for n, c in enumerate(line, 1):
            l = int(c)
            if n % 2:
                # odd number, file slot
                if l:
                    files[j] = {"length": l, "id": i}
            else:
                if l:
                    frees[j] = {"length": l}
                i += 1
            j += l
    return (files, frees, j)


def part_1():
    (files, frees, max_idx) = process()
    j = 0
    vals = []
    while j < max_idx:
        if j in files:
            vals.extend([files[j]["id"]] * files[j]["length"])
        elif j in frees:
            vals.extend(["."] * frees[j]["length"])
        j += 1
    debug(f"{vals=}")
    while True:
        if "." not in vals:
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
