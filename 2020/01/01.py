import common
import itertools

import pyperclip

TEST = True

if TEST:
    input_data = common.test_data
else:
    input_data = common.input_data

if 1:
    # Part 1
    for idx in range(0, len(input_data)):
        for second in input_data[idx + 1 :]:
            first = input_data[idx]
            if first + second == 2020:
                print(first, second, first * second)
                pyperclip.copy(first * second)
                break
