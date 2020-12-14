from collections import defaultdict
import pprint

import common
from common import debug
import settings


def process():
    groups = [[defaultdict(int),]]
    n = 0
    input_data = common.read_string_file()
    for l in input_data:
        if l:
            n += 1
            for c in l:
                groups[-1][0][c] += 1
        else:
            groups[-1].append(n)
            n = 0
            groups.append(
                [defaultdict(int),]
            )
    groups[-1].append(n)
    return groups


def part_1():
    groups = process()
    lens = [len(d.keys()) for (d, num) in groups]
    debug(groups, pretty=True)
    debug(lens)
    debug(sum(lens))
    return sum(lens)


def part_2():
    groups = process()
    lens = [len([k for (k, v) in d.items() if v == num]) for (d, num) in groups]
    debug(groups, pretty=True)
    debug(lens)
    debug(sum(lens))
    return sum(lens)
