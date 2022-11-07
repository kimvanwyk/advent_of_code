import attr

import common
from common import debug
from copy import copy, deepcopy
import settings

import itertools
import sys

INDICES = {0: 1, 1: 0}

POSSIBLE_ROLLS = [sum(i) for i in (itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)))]

WINNERS = {0: 0, 1: 0}


@attr.define
class DeterministicDie:
    sides: int
    val: int = 0
    rolls: int = 0

    def roll(self):
        self.rolls += 1
        self.val += 1
        if self.val > self.sides:
            self.val = 1
        return self.val


@attr.define
class Player:
    pos: int
    score: int = 0

    def forward(self, steps, test=False):
        pos = self.pos + steps
        pos %= 10
        if pos == 0:
            pos = 10
        score = self.score + pos
        if test:
            return score
        self.pos = pos
        self.score = score
        return self.score


@attr.define
class Universe:
    players: tuple
    index: int = 0
    target: int = 1000
    won: bool = False

    def __attrs_post_init__(self):
        self.index = 1

    def forward(self, steps, test=False):
        self.index = INDICES[self.index]
        player = self.players[self.index]
        score = player.forward(steps, test)
        if test:
            # revert index as just a test
            self.index = INDICES[self.index]
            return score >= self.target
        # debug(f"{steps=}, {player=}")
        self.won = score >= self.target
        return self.won


def get_players():
    input_data = common.read_string_file()
    players = tuple([Player(int(l.split(":")[-1].strip())) for l in input_data])
    debug(players)
    return players


def part_1():
    die = DeterministicDie(100)
    debug(die)

    universe = Universe(players=get_players())
    while True:
        if universe.forward(sum([die.roll() for n in range(3)])):
            break
    loser_index = INDICES[universe.index]
    debug(f"{universe.players[loser_index]=}, {die=}")

    return universe.players[loser_index].score * die.rolls


def roll(p1_pos, p1_score, p2_pos, p2_score, index):
    if index:
        pos = p2_pos
        score = p2_score
    else:
        pos = p1_pos
        score = p1_score
    for steps in POSSIBLE_ROLLS:
        pos += steps
        pos %= 10
        if pos == 0:
            pos = 10
        score += pos
        if score >= 21:
            WINNERS[index] += 1
        else:
            if index:
                p2_pos = pos
                p2_score = score
            else:
                p1_pos = pos
                p1_score = score
            roll(p1_pos, p1_score, p2_pos, p2_score, INDICES[index])


def part_2():
    players = get_players()
    sys.setrecursionlimit(50000)
    roll(players[0].pos, 0, players[1].pos, 0, 0)
    print(WINNERS)
    return ""
