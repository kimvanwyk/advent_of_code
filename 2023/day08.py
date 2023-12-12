import common
from common import debug
import settings

from rich import print

DIR_INDEX = {"L": 0, "R": 1}


def process(currents=None):
    node_map = {}
    for l in common.read_string_file():
        if l:
            if "=" in l:
                (k, nodes) = [c.strip() for c in l.split("=")]
                (left, right) = [c.strip() for c in nodes[1:-1].split(",")]
                node_map[k] = (left, right)
            else:
                directions = [DIR_INDEX[c] for c in l.strip()]
    debug(directions)
    debug(node_map)
    if currents is None:
        currents = {node: node for node in node_map.keys() if node[-1] == "A"}
    debug(currents)
    n = 0
    done = False
    while not done:
        for d in directions:
            n += 1
            debug((n, d, currents))
            for start, current in currents.items():
                currents[start] = node_map[current][d]
            if all(current[-1] == "Z" for current in currents.values()):
                done = True
                break
    return n


def part_1():
    return process(["AAA"])


def part_2():
    return process()
