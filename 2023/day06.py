import common
from common import debug
import settings

from rich import print


def process():
    vals = []
    for l in common.read_string_file():
        if l:
            vals.append([int(v.strip()) for v in l.split(":")[-1].strip().split()])
    return list(zip(*vals))


def part_1():
    races = process()
    debug(races)
    num_ways = []
    for time, distance in races:
        ways = 0
        for t in range(1, time):
            if ((time - t) * t) > distance:
                ways += 1
            else:
                if ways:
                    num_ways.append(ways)
                    break
        debug(num_ways)
        mult = 1
        for ways in num_ways:
            mult *= ways
    return mult


def part_2():
    return process()
