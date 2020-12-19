import common
from common import debug
import settings


def process():
    input_data = common.read_string_file()
    for line in input_data:
        yield [int(i) for i in line.split(",")]


def find_last_num(target_idx=2020):
    results = []
    for (data, start_nums) in enumerate(process()):
        nums = {}
        n = 1
        last_num = None
        for sn in start_nums:
            if n > 1:
                nums[last_num] = n - 1
            last_num = sn
            n += 1
        while True:
            if last_num not in nums:
                nums[last_num] = n - 1
                last_num = 0
            else:
                ln = last_num
                last_num = n - 1 - nums[last_num]
                nums[ln] = n - 1
            n += 1
            if n == (target_idx + 1):
                results.append(last_num)
                break
        debug(f"Round {data}: {target_idx} last num: {results[-1]}")
    return results


def part_1():
    results = find_last_num(2020)
    return results[0]


def part_2():
    results = find_last_num(30000000)
    return results[0]
