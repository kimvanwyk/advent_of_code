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
P1_MAPPINGS = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

P2_MAPPINGS = {
    "X": {"rock": SCISSORS, "paper": ROCK, "scissors": PAPER},
    "Y": {"rock": ROCK, "paper": PAPER, "scissors": SCISSORS},
    "Z": {"rock": PAPER, "paper": SCISSORS, "scissors": ROCK},
}


def process():
    input_data = common.read_string_file()
    return input_data


def part_1():
    total = 0
    for line in process():
        if line:
            bout = [P1_MAPPINGS[item] for item in line.split(" ")]
            debug(f"{bout=} {bout[1].play(bout[0])=}")
            total += bout[1].play(bout[0])
    return str(total)


def part_2():
    total = 0
    for line in process():
        if line:
            items = line.split(" ")
            opp = P1_MAPPINGS[items[0]]
            own = P2_MAPPINGS[items[1]][opp.description]
            debug(f"{items[1]=} {own=} {opp=} {own.play(opp)=}")
            total += own.play(opp)
    return str(total)
