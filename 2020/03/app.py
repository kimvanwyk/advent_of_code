import sys

import attr
import pyperclip

sys.path.insert(0, "../")
import common

TEST = 0
DEBUG = 0

if TEST:
    input_data = common.read_string_file("test_data.txt")
else:
    input_data = common.read_string_file("input.txt")


@attr.s
class InputData:
    input_data = attr.ib(default=input_data)
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
        for row in self.parse_input_data():
            yield (self.x in row)
            self.advance()


i = InputData()
hits = 0
for (row, hit) in enumerate(i.is_tree_in_row()):
    if DEBUG:
        print(row, hit, i.x)
    if hit:
        hits += 1
print(hits)
