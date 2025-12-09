import common
from common import debug
import settings

from rich import print

from itertools import combinations
import math


def process():
    points = {}
    for n, l in enumerate(common.read_string_file()):
        points[n] = tuple([int(c) for c in l.split(",")])
    return points


def get_distance(p1, p2):
    return math.sqrt(sum([math.pow((b - a), 2) for (a, b) in zip(p1, p2)]))


def part_1():
    points = process()
    debug(points)
    distances = []
    for combination in combinations(points.keys(), r=2):
        (p1, p2) = (points[combination[0]], points[combination[1]])
        distances.append(
            (
                get_distance(points[combination[0]], points[combination[1]]),
                p1,
                p2,
                *combination,
            )
        )
    distances.sort()
    debug(distances[:5])


def part_2():
    return process()
