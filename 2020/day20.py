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


def layout_tiles(tiles):
    pairs = []
    edges = {}
    for (t1, t2) in combinations(tiles.keys(), 2):
        edges1 = edges.setdefault(t1, get_edges(tiles[t1]))
        edges2 = edges.setdefault(t2, get_edges(tiles[t2]))
        for (s1, e1) in edges1:
            for (s2, e2) in edges2:
                if e1 == e2:
                    pairs.append(((t1, s1, False), (t2, s2, False)))
                elif e1 == e2[::-1]:
                    pairs.append(((t1, s1, False), (t2, s2, True)))

    # map sides to rotations
    rotations = {
        ("l", "r"): 0,
        ("l", "t"): 90,
        ("l", "l"): 180,
        ("l", "b"): 270,
        ("t", "b"): 0,
        ("t", "r"): 90,
        ("t", "t"): 180,
        ("t", "l"): 270,
        ("r", "l"): 0,
        ("r", "b"): 90,
        ("r", "r"): 180,
        ("r", "t"): 270,
        ("b", "t"): 0,
        ("b", "l"): 90,
        ("b", "b"): 180,
        ("b", "r"): 270,
    }
    # map t1 sides to position of next tile
    positions = {"l": (-1, 0), "b": (0, -1), "r": (1, 0), "t": (0, 1)}

    layout = {pairs[0][0][0]: (100, 100)}
    while True:
        skipped = False
        for ((t1, s1, f1), (t2, s2, f2)) in pairs:
            if t1 not in layout:
                skipped = True
            else:
                (x1, y1) = layout[t1]
                (x2, y2) = positions[s1]
                layout[t2] = (x1 + x2, y1 + y2)
                print(
                    f"{t1} {s1} -> {s2} {t2} (flipped: {f2}). Rotation: {rotations[(s1, s2)]}; positions: {layout[t2]}"
                )
        if not skipped:
            break
    print(layout)


def part_1():
    tiles = process()
    edge_counts = find_unique_edge_count(tiles)
    return prod(tid for (tid, count) in edge_counts.items() if count == 2)


def part_2():
    tiles = process()
    pairs = layout_tiles(tiles)
    return pairs
