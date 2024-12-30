import common
from common import debug
import settings

from rich import print

from collections import defaultdict
from pathlib import Path


def process():
    d = defaultdict(int)
    for l in common.read_string_file():
        for c in l.split(" "):
            d[c] += 1
    debug(d)
    return d


def run_steps(num_steps: int):
    d = process()
    steps = 0
    while steps < num_steps:
        nd = defaultdict(int)
        noughts = d["0"]
        d["0"] = 0
        keys = list(d.keys())
        for k in keys:
            v = d[k]
            if v:
                if not len(k) % 2:
                    sp = int(len(k) / 2)
                    left = str(int(k[:sp]))
                    right = str(int(k[sp::]))
                    nd[left] += d[k]
                    nd[right] += d[k]
                else:
                    nd[str(int(k) * 2024)] += v
        nd["1"] += noughts
        if steps < 6:
            debug(nd)
        d = nd
        steps += 1
    return sum(nd.values())


def part_1():
    return run_steps(25)


def part_2():
    return run_steps(75)
