import common
from common import debug
import settings


def process():
    return common.read_string_file()


def part_1():
    pairs = []
    subsets = 0
    for line in process():
        pairs = [[int(i) for i in rng.split("-")] for rng in line.split(",")]
        if (pairs[0][0] <= pairs[1][0] <= pairs[1][1] <= pairs[0][1]) or (
            pairs[1][0] <= pairs[0][0] <= pairs[0][1] <= pairs[1][1]
        ):
            subsets += 1
            debug(pairs)
            debug(f"found match.")
    return subsets


def part_2():
    pairs = []
    subsets = 0
    for line in process():
        pairs = [[int(i) for i in rng.split("-")] for rng in line.split(",")]
        pairs.sort()
        if pairs[0][1] >= pairs[1][0]:
            subsets += 1
            debug(pairs)
            debug(f"found match.")
    return subsets
