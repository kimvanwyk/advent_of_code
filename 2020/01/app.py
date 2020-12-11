import itertools
import math
import sys

import pyperclip

sys.path.insert(0, "../")
import common

TEST = 0
test_data = [1721, 979, 366, 299, 675, 1456]

if TEST:
    input_data = (i for i in test_data)
else:
    input_data = common.read_integer_file("input.txt")

# Part 1: split = 2; total = 2020
# Part 1: split = 3; total = 2020
split = 3
total = 2020

for t in itertools.combinations(input_data, split):
    if sum(t) == total:
        print(t, math.prod(t))
        pyperclip.copy(math.prod(t))
        break
