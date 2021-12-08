import common
from common import debug
import settings

import attr


@attr.s
class Display:
    signals = attr.ib(default=list)
    segments = attr.ib(default=list)

    def set_from_input_line(self, input_line):
        for (attr, items) in zip(("signals", "segments"), input_line.split("|")):
            setattr(self, attr, [s.strip() for s in items.split(" ") if s.strip()])

    def count_matching_segment_lengths(self, lengths):
        return len([s for s in self.segments if len(s) in lengths])


def process():
    input_data = common.read_string_file()
    displays = []
    for line in input_data:
        d = Display()
        d.set_from_input_line(line)
        displays.append(d)
    debug(displays)
    return displays


def part_1():
    displays = process()
    # find sum of 1s, 4s, 7s and 8s (with segment length of 2, 3, 4 and 7 respectively
    counts = [d.count_matching_segment_lengths((2, 4, 3, 7)) for d in displays]
    debug(counts)
    return sum(counts)


def part_2():
    return process()
