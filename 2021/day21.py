import attr

import common
from common import debug
from copy import deepcopy
import settings

import itertools

INDICES = {0: 1, 1: 0}


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


def part_2():
    u = Universe(players=get_players(), target=21)
    universes = {id(u): u}
    winners = {0: 0, 1: 0}
    n = 0
    possible_rolls = [
        sum(i) for i in (itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)))
    ]
    debug(universes)
    while True:
        n += 1
        if not universes:
            break
        for (key, universe) in list(universes.items()):
            del universes[key]
            for roll in possible_rolls:
                if universe.forward(roll, test=True):
                    winners[universe.index] += 1
                else:
                    new = deepcopy(universe)
                    new.forward(roll)
                    universes[id(new)] = new
        if n < 6:
            debug(universes)
            debug(len(universes))
            debug("")
        else:
            break
    print(n)
    print(winners)
    return ""
