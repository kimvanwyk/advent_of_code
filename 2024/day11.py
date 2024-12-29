import common
from common import debug
import settings

from rich import print

import pathlib


def process():
    for p in pathlib(".").glob("step*.txt"):
        p.unlink(missing_ok=True)
    for l in common.read_string_file():
        with open("step000.txt", "w") as fh:
            for c in l.split(" "):
                fh.write(f"{c}\n")


def run_steps(num_steps: int):
    stones = process()
    debug(stones)

    steps = 0
    while steps < num_steps:
        k = 0
        while k < len(stones):
            v = stones[k]
            if v == "0":
                stones[k] = "1"
            elif not len(v) % 2:
                sp = int(len(v) / 2)
                left = v[:sp]
                right = v[sp::]
                stones[k : k + 1] = (str(int(left)), str(int(right)))
                k += 1
            else:
                stones[k] = str(int(v) * 2024)
            k += 1
        if steps < 6:
            debug(stones)
        steps += 1
    return len(stones)


def part_1():
    process()
    # return run_steps(25)


def part_2():
    return run_steps(75)
