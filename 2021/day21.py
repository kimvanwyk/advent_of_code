import attr

import common
from common import debug
from copy import deepcopy
import settings

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

    def forward(self, steps):
        self.pos += steps
        self.pos %= 10
        if self.pos == 0:
            self.pos = 10
        self.score += self.pos


@attr.define
class Universe:
    players: tuple
    index: int = 0
    target: int = 1000
    won: bool = False
    rolls: list = []

    def __attrs_post_init__(self):
        self.index = 1

    def forward(self, steps):
        self.index = INDICES[self.index]
        player = self.players[self.index]
        player.forward(steps)
        debug(f"{steps=}, {player=}")
        self.won = player.score >= self.target
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
    while True:
        n += 1
        found = False
        # for (key, universe) in [
        #     items for items in universes.items() if not items[-1].won
        # ]:
        #     found = True
        #     del universes[key]
        #     for roll in possible_rolls()
        #     new_universes = {}
        #     for roll in range(1, 4):
        #         new = deepcopy(universe)
        #         new.record_roll(roll)
        #         new_universes[id(new)] = new

        #     for extra_loops in range(2):
        #         for (key, universe) in list(new_universes.items()):
        #             del new_universes[key]
        #             for roll in range(1, 4):
        #                 new = deepcopy(universe)
        #                 new.record_roll(roll)
        #                 new_universes[id(new)] = new

        #     for (key, universe) in new_universes.items():
        #         if universe.forward():
        #             winners[universe.index] += 1
        #         else:
        #             universes[key] = universe

        # if not found:
        #     print(n)
        #     print(winners)
        #     break
    return ""
