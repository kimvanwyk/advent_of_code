import common
from common import debug
import settings

from rich import print


class Processor:
    def process(self):
        self.ranges = {}
        for l in common.read_string_file():
            if "-" in l:
                self.ranges[tuple([int(num) for num in l.split("-")])] = 1
            elif l:
                yield (int(l))


def part_1():
    processor = Processor()
    num_fresh = 0
    for ingredient in processor.process():
        for start, end in processor.ranges:
            if start <= ingredient <= end:
                debug(f"Ingredient {ingredient} in range ({start}, {end})")
                num_fresh += 1
                break
    return num_fresh


def part_2():
    return process()
