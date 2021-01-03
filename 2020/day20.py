from collections import defaultdict
from itertools import combinations
from math import prod

import numpy

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
            array = []
        elif line:
            array.append([c for c in line])
        else:
            tiles[tid] = numpy.array(array)
    if array:
        tiles[tid] = numpy.array(array)

    return tiles


def show(tile):
    for row in tile:
        debug("".join(row))


def get_edges(tile):
    edges = [
        (side, list(t))
        for (side, t) in [
            ("t", tile[0, :]),
            ("b", tile[-1, :]),
            ("l", tile[:, 0]),
            ("r", tile[:, -1]),
        ]
    ]
    return edges


def find_unique_edge_count(tiles):
    edge_counts = defaultdict(int)
    edges = {}
    for (t1, t2) in combinations(tiles.keys(), 2):
        edges1 = edges.setdefault(t1, get_edges(tiles[t1]))
        edges2 = edges.setdefault(t2, get_edges(tiles[t2]))
        for (_, e1) in edges1:
            for (_, e2) in edges2:
                if (e1 == e2) or (e1 == e2[::-1]):
                    edge_counts[t1] += 1
                    edge_counts[t2] += 1
    return edge_counts


def find_layout(tiles):
    pairs = []
    edges = {}
    for (t1, t2) in combinations(tiles.keys(), 2):
        edges1 = edges.setdefault(t1, get_edges(tiles[t1]))
        edges2 = edges.setdefault(t2, get_edges(tiles[t2]))
        for (s1, e1) in tiles[t1].items():
            for (s2, e2) in tiles[t2].items():
                if e1 == e2:
                    pairs.append(((t1, s1, False), (t2, s2, False)))
                elif e1 == e2[::-1]:
                    pairs.append(((t1, s1, False), (t2, s2, True)))
    return pairs


def part_1():
    tiles = process()
    edge_counts = find_unique_edge_count(tiles)
    return prod(tid for (tid, count) in edge_counts.items() if count == 2)


def part_2():
    tiles = process()
    pairs = find_layout(tiles)
    return pairs
