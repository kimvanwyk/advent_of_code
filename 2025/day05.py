import common
from common import debug
import settings

from rich import print


class Processor:
    def set_ranges(self):
        self.ranges = {}
        for l in common.read_string_file():
            if "-" in l:
                self.ranges[tuple([int(num) for num in l.split("-")])] = 1

    def yield_ingredients(self):
        for l in common.read_string_file():
            if l and "-" not in l:
                yield (int(l))


def part_1():
    processor = Processor()
    processor.set_ranges()
    num_fresh = 0
    for ingredient in processor.yield_ingredients():
        for start, end in processor.ranges:
            if start <= ingredient <= end:
                debug(f"Ingredient {ingredient} in range ({start}, {end})")
                num_fresh += 1
                break
    return num_fresh


def part_2():
    num_fresh = 0
    processor = Processor()
    processor.set_ranges()
    ranges = list(processor.ranges.keys())
    ranges.sort()
    debug(ranges)

    (start, end) = ranges[0]
    for range_start, range_end in ranges[1:]:
        debug(start, end, num_fresh)
        if range_start > end:
            # end of a range
            num_fresh += end - start + 1
            (start, end) = (range_start, range_end)
        else:
            if range_end > end:
                end = range_end
        debug(start, end, num_fresh)
    num_fresh += end - start + 1
    return num_fresh
