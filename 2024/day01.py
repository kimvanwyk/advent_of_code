from collections import Counter
import common
from common import debug
import settings

from rich import print


def process():
    l1 = []
    l2 = []
    for line in common.read_string_file():
        (i, j) = [int(c.strip()) for c in line.split(" ", 1)]
        l1.append(i)
        l2.append(j)
    return (l1, l2)


def part_1():
    (l1, l2) = process()
    l1.sort()
    l2.sort()
    debug(l1, l2)
    sum = 0
    for i, j in zip(l1, l2):
        sum += abs(j - i)
    return sum


def part_2():
    (l1, l2) = process()
    c = Counter(l2)
    debug(c)

    sum = 0
    for i in l1:
        if i in c:
            sum += i * c[i]
    return sum
