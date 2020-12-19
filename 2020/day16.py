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
    own = attr.ib(default=None)

    def parse(self):
        self.fields = {}
        self.input_data = common.read_string_file()
        patterns = True
        for line in self.input_data:
            if patterns:
                m = FIELD_RE.match(line)
                if m:
                    d = m.groupdict()
                    self.fields[d["field"]] = (
                        (int(d["min1"]), int(d["max1"])),
                        (int(d["min2"]), int(d["max2"])),
                    )
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


def process():
    input_data = InputData()
    input_data.parse()
    debug(f"fields: {input_data.fields}")
    debug(f"own: {input_data.own}")
    for other in input_data.yield_others():
        debug(f"other: {other}")
    return ""


def part_1():
    return process()


def part_2():
    return process()
