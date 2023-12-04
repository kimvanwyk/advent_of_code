import common
from common import debug
import settings

from rich import print


def process():
    for l in common.read_string_file():
        [name, nums] = l.split(": ")
        name = int(name.split(" ")[-1])
        results = [name]
        for num_string in nums.split("|"):
            results.append(set([int(n) for n in num_string.strip().split(" ") if n]))
        yield results


def part_1():
    points = 0
    for name, winning, held in process():
        debug((name, winning, held))
        intersection = winning.intersection(held)
        debug(intersection)
        if intersection:
            points += 2 ** (len(intersection) - 1)
    return points


def part_2():
    return process()
