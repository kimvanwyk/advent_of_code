import math

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
    steps = []
    for start in currents:
        dn = 0
        steps.append([])
        rounds = 3
        current = start
        while rounds:
            done = False
            n = 0
            while not done:
                current = node_map[current][directions[dn]]
                debug(current)
                dn += 1
                if dn >= len(directions):
                    dn = 0
                n += 1
                if current[-1] == "Z":
                    steps[-1].append(n)
                    rounds -= 1
                    done = True
    debug(steps)
    return steps


def part_1():
    steps = process(["AAA"])
    return steps[0][0]


def part_2():
    steps = process()
    print(steps)
    return math.lcm(*[s[0] for s in steps])
