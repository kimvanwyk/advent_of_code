from itertools import combinations

import common
import settings


def part_1(window_size=25, debug=settings.settings.debug):
    if settings.settings.test:
        window_size = 5
    input_data = [n for n in common.read_integer_file()]
    for n in range(window_size, len(input_data)):
        found = False
        for (a, b) in combinations(input_data[n - window_size : n], 2):
            if debug:
                print(
                    f"a: {a}, b: {b}, a != b: {a != b}, a + b: {a + b}, val: {input_data[n]}, match: {a + b == input_data[n]}"
                )
            if a != b:
                if a + b == input_data[n]:
                    found = True
                    break
        if not found:
            if debug:
                print("No match: ", input_data[n])
            break

    if not found:
        return input_data[n]
    return "Not found"


def part_2():
    target = part_1(debug=False)
    input_data = [n for n in common.read_integer_file()]
    nums = []
    found = False
    start = 0
    while start < len(input_data):
        n = start
        nums = []
        while True:
            nums.append(input_data[n])
            if sum(nums) > target:
                found = False
                break
            if sum(nums) == target:
                found = True
                break
            n += 1
        if found:
            break
        start += 1

    if found:
        result = min(nums) + max(nums)

        if settings.settings.debug:
            print(start)
            print(nums)
            print(result)
    else:
        result = "Not found"
    return result
