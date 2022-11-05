import attr

import common
from common import debug
import settings


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


def process():
    input_data = common.read_string_file()
    players = [Player(int(l.split(":")[-1].strip())) for l in input_data]
    debug(players)
    die = DeterministicDie(100)
    debug(die)

    n = 0
    player_index = 1
    # while n < 8:
    while True:
        player_index = 0 if player_index else 1
        player = players[player_index]
        roll = sum([die.roll() for n in range(3)])
        player.forward(roll)
        debug(f"{roll=}, {player=}")
        n += 1

        if player.score >= 1000:
            break
    loser_index = 0 if player_index else 1
    debug(f"{players[loser_index]=}, {die=}")
    return players[loser_index].score * die.rolls


def part_1():
    return process()


def part_2():
    return process()
