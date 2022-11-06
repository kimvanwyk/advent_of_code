import attr

import common
from common import debug
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
    players: list
    index: int = 0

    def __attrs_post_init__(self):
        self.index = 1

    def forward(self, steps):
        self.index = INDICES[self.index]
        player = self.players[self.index]
        player.forward(steps)
        debug(f"{steps=}, {player=}")
        return player.score >= 1000


def get_players():
    input_data = common.read_string_file()
    players = [Player(int(l.split(":")[-1].strip())) for l in input_data]
    debug(players)
    return players


def part_1():
    die = DeterministicDie(100)
    debug(die)

    universe = Universe(players=get_players())
    while True:
        roll = sum([die.roll() for n in range(3)])
        if universe.forward(roll):
            break
    loser_index = INDICES[universe.index]
    debug(f"{universe.players[loser_index]=}, {die=}")

    return universe.players[loser_index].score * die.rolls


def part_2():
    return process()
