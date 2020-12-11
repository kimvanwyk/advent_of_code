import common
import itertools

import pyperclip

TEST = 0

if TEST:
    input_data = common.test_data
else:
    input_data = common.input_data

if 1:
    # Part 1
    for (first, second) in itertools.combinations(input_data, 2):
        if first + second == 2020:
            print(first, second, first * second)
            pyperclip.copy(first * second)
            break
