import common
from common import debug
import settings

from attr import define


TYPES = ["rock", "paper", "scissors"]

COMPARISONS = {
    "rock": {"rock": 3, "scissors": 6, "paper": 0},
    "paper": {"rock": 6, "scissors": 0, "paper": 3},
    "scissors": {"rock": 0, "scissors": 3, "paper": 6},
}


@define
class Hand:
    score: int
    description: str

    def play(self, other_hand):
        return self.score + COMPARISONS[self.description][other_hand.description]


ROCK = Hand(score=1, description="rock")
PAPER = Hand(score=2, description="paper")
SCISSORS = Hand(score=3, description="scissors")
MAPPINGS = {"A": ROCK, "B": PAPER, "C": SCISSORS, "X": ROCK, "Y": PAPER, "Z": SCISSORS}


def process():
    input_data = common.read_string_file()
    return input_data


def part_1():
    total = 0
    for line in process():
        if line:
            bout = [MAPPINGS[item] for item in line.split(" ")]
            debug(f"{bout=} {bout[1].play(bout[0])=}")
            total += bout[1].play(bout[0])
    return str(total)


def part_2():
    return process()
