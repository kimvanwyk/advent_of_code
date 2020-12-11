import common
import itertools
import math

import pyperclip

TEST = 0

if TEST:
    input_data = common.test_data
else:
    input_data = common.input_data

# Part 1: split = 2
split = 2

for t in itertools.combinations(input_data, split):
    if sum(t) == 2020:
        print(t, math.prod(t))
        pyperclip.copy(math.prod(t))
        break
