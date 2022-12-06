import common
from common import debug
import settings

from collections import deque


def process(msglen):
    indices = []
    for line in common.read_string_file():
        d = deque(maxlen=msglen)
        d.extend(line[: msglen - 1])
        debug(d)
        for (n, c) in enumerate(line[msglen - 1 :], msglen):
            d.append(c)
            debug(f"{n=} {c=} {d=}")
            if len(set(d)) == msglen:
                indices.append(n)
                break
    return indices


def part_1():
    print(process(4))
    return ""


def part_2():
    print(process(14))
    return ""
