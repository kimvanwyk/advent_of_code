import common
from common import debug
import settings

from collections import deque


def process():
    return common.read_string_file()


def part_1():
    indices = []
    for line in process():
        d = deque(maxlen=4)
        d.extend(line[:3])
        debug(d)
        for (n, c) in enumerate(line[3:], 4):
            d.append(c)
            debug(f"{n=} {c=} {d=}")
            if len(set(d)) == 4:
                indices.append(n)
                break
    print(indices)
    return ""


def part_2():
    return process()
