import common
from common import debug
import settings

from rich import print

from collections import defaultdict


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
    cards = {}
    for num_cards, (name, winning, held) in enumerate(process(), 1):
        debug((name, winning, held))
        cards[name] = len(winning.intersection(held))
    debug(cards)
    debug(num_cards)

    tracking = defaultdict(lambda: 1)
    for n in range(1, num_cards + 1):
        if n not in tracking:
            tracking[n] = 1
        for c in range(n + 1, n + cards[n] + 1):
            tracking[c] += tracking[n]
        debug((n, c, tracking))
    debug(tracking)
    return sum(tracking.values())
