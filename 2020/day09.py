from itertools import combinations

import common
import settings


def process(window_size=25):
    if settings.settings.test:
        window_size = 5
    input_data = [n for n in common.read_integer_file()]
    for n in range(window_size, len(input_data)):
        print(n)
        found = False
        for (a, b) in combinations(input_data[n - window_size : n], 2):
            if settings.settings.debug:
                print(
                    f"a: {a}, b: {b}, a != b: {a != b}, a + b: {a + b}, val: {input_data[n]}, match: {a + b == input_data[n]}"
                )
            if a != b:
                if a + b == input_data[n]:
                    found = True
                    break
        if not found:
            if settings.settings.debug:
                print("No match: ", input_data[n])
            break

    if not found:
        return input_data[n]
    return "Not found"


def part_1():
    return process()


def part_2():
    return process()
