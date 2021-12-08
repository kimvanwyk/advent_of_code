from collections import Counter

import common
from common import debug
import settings

import attr

# Segment numbering:

#  111
# 2   3
# 2   3
#  444
# 5   6
# 5   6
#  777

SEGMENT_LENGTHS = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
SEGMENTS = {
    (1, 2, 3, 5, 6, 7): 0,
    (3, 6): 1,
    (1, 3, 4, 5, 7): 2,
    (1, 3, 4, 6, 7): 3,
    (2, 3, 4, 6): 4,
    (1, 2, 4, 6, 7): 5,
    (1, 2, 4, 5, 6, 7): 6,
    (1, 3, 6): 7,
    (1, 2, 3, 4, 5, 6, 7): 8,
    (1, 2, 3, 4, 6, 7): 9,
}


@attr.s
class Display:
    signals = attr.ib(default=list)
    segments = attr.ib(default=list)

    def set_from_input_line(self, input_line):
        for (attr, items) in zip(("signals", "segments"), input_line.split("|")):
            setattr(self, attr, [s.strip() for s in items.split(" ") if s.strip()])
            setattr(
                self, f"{attr}_sets", [set([c for c in s]) for s in getattr(self, attr)]
            )
        self.all = self.signals + self.segments
        self.all_sets = self.signals_sets + self.segments_sets

    def count_matching_segment_lengths(self, lengths):
        return len([s for s in self.segments if len(s) in lengths])

    def get_chars_of_length(self, length):
        return [c for c in [d for d in self.all if len(d) == length][0]]

    def length_subsets(self, chars, length, only_unmatched=False):
        """Return vals if vals of length from self.all has all the chars in chars
        if only_unmatched return just the chars that aren't in the input chars"""
        if not only_unmatched:

            def f(val):
                return val

        else:

            def f(val):
                return val.difference(set(chars))

        return [
            f(val)
            for val in self.all_sets
            if len(val) == length and set(chars).issubset(val)
        ]

    def get_non_matching_char_sets(self, chars):
        """Return any sets of chars of the same length as the chars input that don't match it"""
        return [c for c in self.all_sets if (len(c) == len(chars)) and (c != chars)]

    def set_segment_value(self):
        vals = []
        for segment_set in self.segments_sets:
            segment = [self.segment_names[s] for s in segment_set]
            segment.sort()
            vals.append(SEGMENTS[tuple(segment)])
        self.segment_value = int("".join(str(v) for v in vals))
        debug(self.segment_value)

    def calculate_segments(self):
        self.segments = {}
        # get chars for D1
        chars = self.get_chars_of_length(SEGMENT_LENGTHS[1])
        self.segments[3] = chars
        self.segments[6] = chars[:]

        # get chars for D7 and diff with S3
        chars = self.get_chars_of_length(SEGMENT_LENGTHS[7])
        self.segments[1] = [c for c in chars if not c in self.segments[3]]

        # get chars for D4 and diff with S3
        chars = self.get_chars_of_length(SEGMENT_LENGTHS[4])
        self.segments[2] = [c for c in chars if not c in self.segments[3]]
        self.segments[4] = self.segments[2][:]

        # any_fives proved all lines have a D5
        # get the chars from the first 5 that aren't in S1 and S2
        five_chars = self.length_subsets(
            self.segments[1] + self.segments[2], SEGMENT_LENGTHS[5]
        )[0]
        unmatched_chars = five_chars.difference(
            set(self.segments[1] + self.segments[2])
        )
        # The overlap between the options for S6 and the unmatched D5 chars must be S6
        self.segments[6] = unmatched_chars.intersection(set(self.segments[6]))

        # S3 mmust be option for S3 that isn't S6
        self.segments[3] = set(self.segments[3]).difference(set(self.segments[6]))

        # S7 must the be the value from the unmatched chars that isn't S6
        self.segments[7] = unmatched_chars.difference(set(self.segments[6]))

        # S5 must be the only unused letter
        used = []
        for v in [list(v) for v in self.segments.values()]:
            used.extend(v)
        self.segments[5] = list(
            set(["a", "b", "c", "d", "e", "f", "g"]).difference(set(used))
        )

        # of the 5-length values, only D5 contains S2 - the intersection of D4's chars and the first of those 5 length values must be D4
        self.segments[4] = self.get_non_matching_char_sets(five_chars)[0].intersection(
            set(self.segments[4])
        )

        # the difference between D2's chars and D4 must be D2
        self.segments[2] = set(self.segments[2]).difference(self.segments[4])

        self.segment_names = {list(v)[0]: k for (k, v) in self.segments.items()}
        debug(self.segments)
        debug(self.segment_names)
        self.set_segment_value()


def process():
    input_data = common.read_string_file()
    displays = []
    for line in input_data:
        if line[0] == "#":
            continue
        d = Display()
        d.set_from_input_line(line)
        displays.append(d)
    debug(displays)
    return displays


def print_must_haves(displays, must_have=(1, 7, 4, 8)):
    for display in displays:
        lengths = Counter([len(d) for d in display.signals + display.segments])
        if not all([SEGMENT_LENGTHS[k] in lengths.keys() for k in must_have]):
            print(lengths.keys())
            print(f"No combo of: {must_have} on at least 1 line")
            break
    else:
        print(f"No lines without: {must_have}")


def any_fives(displays):
    possibilities = {}
    for display in displays:
        # get chars for D1
        chars = display.get_chars_of_length(SEGMENT_LENGTHS[1])
        possibilities[3] = chars
        possibilities[6] = chars[:]

        # get chars for D7 and diff with S3
        chars = display.get_chars_of_length(SEGMENT_LENGTHS[7])
        possibilities[1] = [c for c in chars if not c in possibilities[3]]

        # get chars for D4 and diff with S3
        chars = display.get_chars_of_length(SEGMENT_LENGTHS[4])
        possibilities[2] = [c for c in chars if not c in possibilities[3]]
        possibilities[4] = possibilities[2][:]

        # confirm if anything 5 long has S1,2,4 in it
        if display.length_subsets(possibilities[1] + possibilities[2], 5):
            count += 1
    print(count)


def part_1():
    displays = process()
    # find sum of 1s, 4s, 7s and 8s (with segment length of 2, 3, 4 and 7 respectively
    counts = [d.count_matching_segment_lengths((2, 4, 3, 7)) for d in displays]
    debug(counts)
    return sum(counts)


def part_2():
    # print_must_haves(displays)
    # any_fives(displays)
    total = 0
    for display in process():
        display.calculate_segments()
        total += display.segment_value
    return total
