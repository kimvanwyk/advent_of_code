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
                    files[i] = {"length": l, "pos": j}
            else:
                if l:
                    frees[i] = {"length": l, "pos": j}
                i += 1
            j += l
    return (files, frees, j)


def part_1():
    (files, frees, max_idx) = process()
    debug(files)
    debug(frees)
    d = {}
    for k, val in files.items():
        for j in range(val["pos"], val["pos"] + val["length"]):
            d[j] = k
    for k, val in frees.items():
        for j in range(val["pos"], val["pos"] + val["length"]):
            d[j] = "."
    j = 0
    vals = []
    while True:
        vals.append(d[j])
        j += 1
        if j not in d:
            break
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
    (files, frees, max_idx) = process()
