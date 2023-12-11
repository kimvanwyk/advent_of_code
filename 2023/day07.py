import common
from common import debug
import settings

from attrs import define, field
from rich import print

from collections import Counter

ORDER_P1 = {
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
ORDER_P2 = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
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

    def _typ(self, cards=None):
        if cards is None:
            cards = self.cards
        s = Counter(cards)
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

    @property
    def typ(self):
        return self._typ()

    @property
    def typ_joker(self):
        cards = self.cards[:]
        s = Counter(cards)
        mc = "A"
        for c, freq in s.most_common():
            if c != "J":
                mc = c
                break
        for n, c in enumerate(cards):
            if c == "J":
                cards[n] = mc
        debug((mc, self.cards, cards))
        return self._typ(cards)


def process(joker=False):
    cards = []
    if joker:
        order = ORDER_P2
    else:
        order = ORDER_P1
    for l in common.read_string_file():
        spl = l.split(" ")
        h = Hand(spl[0], int(spl[1]))
        cards.append(h)
    # debug(
    #     (
    #         getattr(h, "typ" if not joker else "typ_joker"),
    #         *[order[c] for c in h.cards],
    #     )
    # )
    cards.sort(
        key=lambda h: (
            getattr(h, "typ" if not joker else "typ_joker"),
            *[order[c] for c in h.cards],
        )
    ),
    # debug(cards)
    mult = 0
    for n, c in enumerate(cards, 1):
        mult += n * c.bid
    return mult


def part_1():
    return process(joker=False)


def part_2():
    return process(joker=True)
