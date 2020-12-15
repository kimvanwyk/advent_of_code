from collections import Counter
import functools

import attr
import networkx

import common
from common import debug
import settings


def process():
    adapters = [n for n in common.read_integer_file()]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters


def part_1():
    adapters = process()
    debug(adapters)
    counter = Counter()
    for n in range(1, len(adapters)):
        counter[adapters[n] - adapters[n - 1]] += 1
    debug(counter)
    return counter[1] * counter[3]

# heavily taken from https://dev.to/qviper/advent-of-code-2020-python-solution-day-10-30kd
# learned some dynamic programming here
def part_2():
    adapters = process()
    total = 0
    paths = {adapters[0]: 1}
    # already seeded first node, skip last as only 1 path to it from second last
    for adapter in adapters[1:-1]:
        paths[adapter] = 0
        for i in (1,2,3):
            if (adapter - i) in paths:
                paths[adapter] += paths[adapter - i]

    print(paths[adapters[-2]])
    return paths[adapters[-2]]
