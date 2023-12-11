import common
from common import debug
import settings

from rich import print

DIR_INDEX = {"L": 0, "R": 1}


def process():
    node_map = {}
    for l in common.read_string_file():
        if l:
            if "=" in l:
                (k, nodes) = [c.strip() for c in l.split("=")]
                (left, right) = [c.strip() for c in nodes[1:-1].split(",")]
                node_map[k] = (left, right)
            else:
                directions = [c for c in l.strip()]
    debug(directions)
    debug(node_map)
    return (directions, node_map)


def part_1():
    (directions, node_map) = process()
    current = "AAA"
    n = 0
    done = False
    while not done:
        for d in directions:
            n += 1
            debug((n, d, current))
            current = node_map[current][DIR_INDEX[d]]
            if current == "ZZZ":
                done = True
                break
    return n


def part_2():
    return process()
