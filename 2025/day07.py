import common
from common import debug
import settings

from rich import print


class Processor:
    def __init__(self):
        self.init_beam_idx = 0
        self.splitter_rows = {}
        self.num_universes = 0
        n = -1
        for l in common.read_string_file():
            if not l:
                break
            n += 1
            splitters = {}
            for idx, c in enumerate(l):
                if c == "S":
                    self.init_beam_idx = idx
                elif c == "^":
                    splitters[idx] = 1
            self.splitter_rows[n] = splitters
        self.max_row = n
        debug([sr.keys() for sr in self.splitter_rows.values()])
        debug(self.max_row)
        debug(self.splitter_rows)

    def process(self):
        for l in common.read_string_file():
            splitters = {}
            for idx, c in enumerate(l):
                if c == "^":
                    splitters[idx] = 1
            yield splitters

    def recurse_path(self, row_idx, beam_idx):
        debug(row_idx, beam_idx, self.num_universes, self.max_row)
        if row_idx >= self.max_row:
            self.num_universes += 1
            return
        if beam_idx not in self.splitter_rows[row_idx + 1]:
            # No spliiter on next row
            self.recurse_path(row_idx + 1, beam_idx)
        else:
            # take both left and right path
            for direction in (-1, 1):
                self.recurse_path(row_idx + 1, beam_idx + direction)


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
    processor = Processor()
    debug(processor.init_beam_idx)
    processor.recurse_path(0, processor.init_beam_idx)
    return processor.num_universes
    # beam_idxs = [processor.init_beam_idx]
    # for row_idx in range(processor.max_row):
    #     debug(row_idx, processor.splitter_rows[row_idx])
    #     next_beam_idxs = []
    #     for beam_idx in beam_idxs:
    #         if beam_idx not in processor.splitter_rows[row_idx + 1]:
    #             next_beam_idxs.append(beam_idx)
    #         else:
    #             next_beam_idxs.append(beam_idx)
