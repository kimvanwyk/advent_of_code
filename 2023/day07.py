import common
from common import debug
import settings

from attrs import define, field
from rich import print

from collections import Counter

ORDER = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

TYPES = {7: "five", 6: "four", 5: "full", 4: "three", 3: "two", 2: "one", 1: "high"}


@define(
    slots=False,
)
class Hand:
    hand: str
    bid: int

    def __attrs_post_init__(self):
        self.cards = [c for c in self.hand]
        self.sorted = self.cards[:]
        self.sorted.sort(key=lambda h: ORDER[h], reverse=True)

    @property
    def typ(self):
        s = Counter(self.cards)
        k = s.values()
        if len(s) == 1:
            return 7
        if 4 in k:
            return 6
        if 3 in k and 2 in k:
            return 5
        if 3 in k and 1 in k:
            return 4
        if len(s) == 3:
            return 3
        if len(s) == 4:
            return 2
        return 1


def process():
    for l in common.read_string_file():
        spl = l.split(" ")
        yield (spl[0], int(spl[1]))


def part_1():
    cards = []
    for hand, bid in process():
        h = Hand(hand, bid)
        t = h.typ
        cards.append(h)
        debug((h, h.sorted, t, TYPES[t], bid))
        debug((h.typ, *[ORDER[c] for c in h.cards]))
    cards.sort(
        key=lambda h: (h.typ, [ORDER[c] for c in h.cards]),
    )
    debug(cards)
    mult = 0
    for n, c in enumerate(cards, 1):
        mult += n * c.bid
    return mult


def part_2():
    return process()
