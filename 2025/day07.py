import common
from common import debug
import settings

from rich import print


class Processor:
    def __init__(self):
        self.init_beam_idx = 0
        for l in common.read_string_file():
            for idx, c in enumerate(l):
                if c == "S":
                    self.init_beam_idx = idx
                    break

    def process(self):
        for l in common.read_string_file():
            splitters = {}
            for idx, c in enumerate(l):
                if c == "^":
                    splitters[idx] = 1
            yield splitters


def part_1():
    processor = Processor()
    debug(processor.init_beam_idx)
    num_splits = 0
    beams = {processor.init_beam_idx: 1}
    for splitters in processor.process():
        debug(splitters.keys())
        next_beams = {}
        for beam_idx in beams:
            # beams are above the current row of splitters
            if beam_idx not in splitters:
                next_beams[beam_idx] = 1
            else:
                num_splits += 1
                next_beams[beam_idx - 1] = 1
                next_beams[beam_idx + 1] = 1
        beams = next_beams
        debug(beams.keys())
    return num_splits


def part_2():
    return process()
