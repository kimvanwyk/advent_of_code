from collections import Counter

import common
from common import debug
import settings


def process():
    adapters = [n for n in common.read_integer_file()]
    return adapters


def part_1():
    adapters = process()
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    debug(adapters)
    counter = Counter()
    for n in range(1, len(adapters)):
        counter[adapters[n] - adapters[n - 1]] += 1
    debug(counter)
    return counter[1] * counter[3]


def part_2():
    return process()
