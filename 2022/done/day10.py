import common
from common import debug
import settings


def process():
    for inst in common.read_string_file():
        if inst == "noop":
            yield None
        if "addx" in inst:
            yield None
            yield int(inst.split(" ")[-1])


def part_1():
    x = 1
    n = 1
    total = 0
    for inst in process():
        if inst is not None:
            x += inst
        n += 1
        if n <= 220 and ((n - 20) % 40 == 0):
            debug(f"{n=} {x=}, {x*n=}")
            total += x * n
    return total


def part_2():
    x = 1
    n = 1
    total = 0
    out = []
    for inst in process():
        if (n - 1) % 40 == 0:
            out.append([])
            pos = 0
        if pos in (x - 1, x, x + 1):
            out[-1].append("#")
        else:
            out[-1].append(".")
        if inst is not None:
            x += inst
        n += 1
        pos += 1
    for row in out:
        print("".join(row))
    return total
