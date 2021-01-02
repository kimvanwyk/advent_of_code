from collections import defaultdict
from itertools import combinations
from math import prod

import common
from common import debug
import settings


def boolify(char):
    return char == "#"


def process():
    input_data = common.read_string_file()
    tiles = {}
    for line in input_data:
        if "Tile" in line:
            tid = int(line[5:-1])
            tiles[tid] = {"t": [], "l": [], "r": [], "b": []}
            n = -1
        else:
            if line:
                if n < 0:
                    length = len(line)
                n += 1
                if n == 0:
                    tiles[tid]["t"] = [boolify(c) for c in line]
                elif n == length - 1:
                    tiles[tid]["b"] = [boolify(c) for c in line]
                tiles[tid]["l"].append(boolify(line[0]))
                tiles[tid]["r"].append(boolify(line[-1]))
    return tiles


def find_unique_edge_count(tiles):
    edges = defaultdict(int)
    for (t1, t2) in combinations(tiles.keys(), 2):
        for e1 in tiles[t1].values():
            for e2 in tiles[t2].values():
                if (e1 == e2) or (e1 == e2[::-1]):
                    edges[t1] += 1
                    edges[t2] += 1
    return edges


def part_1():
    tiles = process()
    edges = find_unique_edge_count(tiles)
    return prod(tid for (tid, edges) in edges.items() if edges == 2)


def part_2():
    return process()
