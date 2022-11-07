import attr

import common
from common import debug
from copy import copy, deepcopy
import settings

from collections import Counter, defaultdict, namedtuple
import itertools

INDICES = {0: 1, 1: 0}

POSSIBLE_ROLLS = Counter(
    [sum(i) for i in (itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)))]
)


WINNERS = {0: 0, 1: 0}
UNIVERSE_KEY = namedtuple("UniverseKey", "p1pos p2pos p1score p2score player won")


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

    def forward(self, steps):
        player = self.players[self.index]
        self.score = player.forward(steps)
        # debug(f"{steps=}, {player=}")
        self.won = score >= self.target
        self.index = INDICES[self.index]
        return self.won


def get_players():
    input_data = common.read_string_file()
    players = tuple([Player(int(l.split(":")[-1].strip())) for l in input_data])
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


def advance_universe(universe, steps):
    pos = [universe.p1pos, universe.p2pos]
    score = [universe.p1score, universe.p2score]
    idx = universe.player
    pos[idx] += steps
    pos[idx] %= 10
    if pos[idx] == 0:
        pos[idx] = 10
    score[idx] += pos[idx]
    return UNIVERSE_KEY(*pos, *score, INDICES[idx], score[idx] >= 21)


# Borrowing the memoisation algorithm from
# https://www.reddit.com/r/adventofcode/comments/wsw4e6/comment/il477vn/?utm_source=share&utm_medium=web2x&context=3
def part_2():
    players = get_players()
    universes = {
        UNIVERSE_KEY(
            players[0].pos, players[1].pos, players[0].score, players[1].score, 0, 0
        ): 1
    }
    debug(POSSIBLE_ROLLS)
    debug(universes)
    found = True
    while found:
        new_universes = defaultdict(int)
        found = False
        for (current_universe, num_universes) in universes.items():
            found = True
            for (steps, num_affected) in POSSIBLE_ROLLS.items():
                new_universe = advance_universe(current_universe, steps)
                # debug((steps, new_universe))
                if new_universe.won:
                    WINNERS[current_universe.player] += num_universes * num_affected
                else:
                    new_universes[new_universe] += num_universes * num_affected
        universes = new_universes
    debug(WINNERS)
    return max(WINNERS.values())
