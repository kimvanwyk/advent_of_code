import common
from common import debug
import settings

from rich import print

from collections import defaultdict
from itertools import combinations
import math


class Processor:
    def __init__(self):
        self.points = {}
        for n, l in enumerate(common.read_string_file()):
            self.points[n] = tuple([int(c) for c in l.split(",")])
        debug(self.points)
        self.circuit_point_map = {}
        self.point_circuit_map = {}
        self.max_num_circuits = 0

    def set_distances(self):
        self.distances = defaultdict(list)
        for combination in combinations(self.points.keys(), r=2):
            self.distances[self.get_distance(*combination)].append(
                combination,
            )

    def get_distance(self, point_idx1, point_idx2):
        return math.sqrt(
            sum(
                [
                    math.pow((b - a), 2)
                    for (a, b) in zip(self.points[point_idx1], self.points[point_idx2])
                ]
            )
        )

    def add_to_circuit(self, point_idxs):
        # debug(self.point_circuit_map)
        (x, y) = (point_idxs[0], point_idxs[1])
        for left, right in ((x, y), (y, x)):
            if left in self.point_circuit_map:
                left_circuit_idx = self.point_circuit_map[left]
                if right not in self.point_circuit_map:
                    # point 2 not in a circuit
                    self.point_circuit_map[right] = left_circuit_idx
                    self.circuit_point_map[left_circuit_idx].append(right)

                    return True

                elif self.point_circuit_map[left] == self.point_circuit_map[right]:
                    # Already in same circuit
                    return False

                else:
                    # right in different circuit, join circuits
                    right_circuit_idx = self.point_circuit_map[right]
                    for point in self.circuit_point_map[right_circuit_idx]:
                        # debug((point, right))
                        self.point_circuit_map[point] = left_circuit_idx
                        self.circuit_point_map[left_circuit_idx].append(point)
                    del self.circuit_point_map[right_circuit_idx]
                    return True

        # New circuit
        self.max_num_circuits += 1
        self.point_circuit_map[point_idxs[0]] = self.max_num_circuits
        self.point_circuit_map[point_idxs[1]] = self.max_num_circuits
        self.circuit_point_map[self.max_num_circuits] = [
            point_idxs[0],
            point_idxs[1],
        ]
        return True

    def build_circuits(self, max_connections=0):
        keys = list(self.distances.keys())
        keys.sort()
        debug(
            [
                (
                    k,
                    self.distances[k],
                    self.points[self.distances[k][0][0]],
                    self.points[self.distances[k][0][1]],
                )
                for k in keys[:12]
            ]
        )

        num_connections = 0
        passes = 0
        while True:
            for distance in keys:
                for point_idxs in self.distances[distance]:
                    passes += 1
                    debug((passes, point_idxs))
                    # if self.add_to_circuit(point_idxs):
                    #     num_connections += 1
                    self.add_to_circuit(point_idxs)
                    num_connections += 1
                    debug(self.circuit_point_map)
                    debug(self.point_circuit_map)
                    debug()
                    if max_connections and (num_connections >= max_connections):
                        return
            break


def part_1():
    processor = Processor()
    processor.set_distances()
    debug(processor.distances)
    processor.build_circuits(1000)
    lens = [len(l) for l in processor.circuit_point_map.values()]
    lens.sort()
    debug(lens)
    return lens[-3] * lens[-2] * lens[-1]


def part_2():
    processor = Processor()
    processor.set_distances()
    debug(processor.distances)
    processor.build_circuits(1000)
    lens = [len(l) for l in processor.circuit_point_map.values()]
    lens.sort()
    debug(lens)
    return lens[-3] * lens[-2] * lens[-1]
