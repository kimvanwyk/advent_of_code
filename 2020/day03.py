import math
import sys

import attr

import common
import settings


@attr.s
class InputData:
    input_data = attr.ib()
    edge = attr.ib(default=None)
    x_amt = attr.ib(default=3)
    y_amt = attr.ib(default=1)
    x = attr.ib(default=0)

    def parse_input_data(self):
        for line in self.input_data:
            if self.edge is None:
                self.edge = len(line)
            yield [idx for (idx, val) in enumerate(line) if val == "#"]

    def advance(self):
        self.x += self.x_amt
        if self.x >= self.edge:
            self.x -= self.edge

    def is_tree_in_row(self):
        n = -1
        rn = 0
        for row in self.parse_input_data():
            rn += 1
            n += 1
            if n < self.y_amt:
                continue
            n = 0
            self.advance()
            yield (self.x in row)


def process(directions):
    hits = []
        input_data = common.read_string_file()
    for (x, y) in directions:
        i = InputData(input_data=input_data, x_amt=x, y_amt=y)
        dir_hits = 0
        for (row, hit) in enumerate(i.is_tree_in_row()):
            if settings.settings.debug:
                print(row, hit, i.x)
            if hit:
                dir_hits += 1
        hits.append(dir_hits)
    result = math.prod(hits)
    return result


def part_1():
    return process(((3, 1),))


def part_2():
    return process(((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))
