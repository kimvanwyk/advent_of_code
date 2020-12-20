import re

import attr

import common
from common import debug
import settings

# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

FIELD_RE = re.compile(
    "(?P<field>.*?): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)"
)


@attr.s
class InputData:
    fields = attr.ib(default=None)
    ranges = attr.ib(default=None)
    own = attr.ib(default=None)

    def parse(self):
        self.fields = {}
        self.ranges = []
        self.input_data = common.read_string_file()
        patterns = True
        for line in self.input_data:
            if patterns:
                m = FIELD_RE.match(line)
                if m:
                    d = m.groupdict()
                    ranges = (
                        range(int(d["min1"]), int(d["max1"]) + 1),
                        range(int(d["min2"]), int(d["max2"]) + 1),
                    )
                    self.fields[d["field"]] = ranges
                    self.ranges.extend(ranges)
                else:
                    break
        for line in self.input_data:
            if "your ticket:" in line:
                continue
            if not line:
                break
            self.own = [int(c.strip()) for c in line.split(",")]

    def yield_others(self):
        for line in self.input_data:
            if "nearby tickets:" in line:
                continue
            if not line:
                break
            other = [int(c.strip()) for c in line.split(",")]
            other.sort()
            yield other


def part_1():
    input_data = InputData()
    input_data.parse()
    debug(f"fields: {input_data.fields}")
    debug(f"own: {input_data.own}")
    invalid_vals = []
    for other in input_data.yield_others():
        for val in other:
            if not any(val in r for r in input_data.ranges):
                invalid_vals.append(val)
                debug(f"Invalid val: {val}")
                break
        debug(f"other: {other}")
    debug(f"Invalid vals: {invalid_vals}")
    return sum(invalid_vals)


def part_2():
    input_data = InputData()
    input_data.parse()
    debug(f"fields: {input_data.fields}")
    debug(f"own: {input_data.own}")
    others = []
    for other in input_data.yield_others():
        if all(any(val in r for r in input_data.ranges) for val in other):
            others.append(other)
    debug(f"others: {others}")
    return ""
