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
    edges = {}
    tiles = {}
    for line in input_data:
        if "Tile" in line:
            tid = int(line[5:-1])
            edges[tid] = {"t": [], "l": [], "r": [], "b": []}
            tiles[tid] = []
            n = -1
        else:
            if line:
                tiles[tid].append([boolify(c) for c in line])
                if n < 0:
                    length = len(line)
                n += 1
                if n == 0:
                    edges[tid]["t"] = [boolify(c) for c in line]
                elif n == length - 1:
                    edges[tid]["b"] = [boolify(c) for c in line]
                edges[tid]["l"].append(boolify(line[0]))
                edges[tid]["r"].append(boolify(line[-1]))
    return (edges, tiles)


def find_unique_edge_count(tiles):
    edges = defaultdict(int)
    for (t1, t2) in combinations(tiles.keys(), 2):
        for e1 in tiles[t1].values():
            for e2 in tiles[t2].values():
                if (e1 == e2) or (e1 == e2[::-1]):
                    edges[t1] += 1
                    edges[t2] += 1
    return edges


def show(tile):
    for row in tile:
        debug("".join("#" if c else "." for c in row))


def find_layout(tiles):
    pairs = []
    for (t1, t2) in combinations(tiles.keys(), 2):
        for (s1, e1) in tiles[t1].items():
            for (s2, e2) in tiles[t2].items():
                if e1 == e2:
                    pairs.append(((t1, s1, False), (t2, s2, False)))
                elif e1 == e2[::-1]:
                    pairs.append(((t1, s1, False), (t2, s2, True)))
    return pairs


def part_1():
    (edges, _) = process()
    edge_counts = find_unique_edge_count(edges)
    return prod(tid for (tid, count) in edge_counts.items() if count == 2)


def part_2():
    (edges, tiles) = process()
    pairs = find_layout(edges)
    show(tiles[2311])
    return pairs
