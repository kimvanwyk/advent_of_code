import common
from common import debug
import settings

from rich import print

import itertools


def process():
    with open(settings.settings.input_file, "r") as fh:
        for r in fh.read().strip().split(","):
            yield (r.split("-"))


def part_1():
    total = 0
    for start, end in process():
        for id_num in range(int(start), int(end) + 1):
            if len(str(id_num)) % 2 == 0:
                h = len(str(id_num)) // 2
                if str(id_num)[:h] == str(id_num)[h:]:
                    total += id_num
                    debug(f"Match {start}-{end}: {id_num}")
    return total


def part_2():
    total = 0
    for start, end in process():
        for id_num in range(int(start), int(end) + 1):
            invalid = False
            for batch_size in range(1, (len(str(id_num)) // 2) + 1):
                batches = [b for b in itertools.batched(str(id_num), n=batch_size)]
                if len(set(batches)) == 1:
                    debug(batches)
                    invalid = True
                    total += id_num
                if invalid:
                    break

    return total
