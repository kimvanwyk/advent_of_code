from collections import defaultdict
import pprint

import common
import settings


def process():
    groups = [defaultdict(int)]
    input_data = common.read_string_file()
    for l in input_data:
        if l:
            for c in l:
                groups[-1][c] += 1
        else:
            groups.append(defaultdict(int))
    return groups


def part_1():
    groups = process()
    lens = [len(d.keys()) for d in groups]
    if settings.settings.debug:
        pprint.pprint(groups)
        print(lens)
        print(sum(lens))
    return sum(lens)


def part_2():
    return process()
