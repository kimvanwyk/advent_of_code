import common
from common import debug
import settings

from rich import print

from itertools import combinations
import math


class Processor:
    def __init__(self):
        self.points = {}
        for n, l in enumerate(common.read_string_file()):
            self.points[n] = tuple([int(c) for c in l.split(",")])
        debug(self.points)

    def set_distances(self):
        self.distances = []
        for combination in combinations(self.points.keys(), r=2):
            self.distances.append(
                (
                    self.get_distance(*combination),
                    (self.points[combination[0]], self.points[combination[1]]),
                    *combination,
                )
            )
        self.distances.sort()

    def get_distance(self, point_idx1, point_idx2):
        return math.sqrt(
            sum(
                [
                    math.pow((b - a), 2)
                    for (a, b) in zip(self.points[point_idx1], self.points[point_idx2])
                ]
            )
        )


def part_1():
    processor = Processor()
    processor.set_distances()
    debug(processor.distances[:5])


def part_2():
    return process()
