import common
from common import debug
import settings

from attrs import define
from rich import print

P1_LIMITS = {"red": 12, "green": 13, "blue": 14}


@define
class Handful:
    red: int = 0
    green: int = 0
    blue: int = 0

    @property
    def p1_valid(self):
        for k, v in P1_LIMITS.items():
            if getattr(self, k) > v:
                return False
        return True

    def set_max(self, other):
        for attr in P1_LIMITS:
            o = getattr(other, attr)
            if getattr(self, attr) < o:
                setattr(self, attr, o)

    @property
    def power(self):
        return self.red * self.green * self.blue


def process():
    for line in common.read_string_file():
        games = []
        gid_string, games_string = line.strip().split(": ")
        gid = int(gid_string.split(" ")[-1])
        for game_string in games_string.split("; "):
            vals = []
            for cube in game_string.split(", "):
                c = cube.split(" ")
                vals.append((c[-1], int(c[0])))
            games.append(Handful(**dict(vals)))
        debug((gid, games))
        yield (gid, games)


def part_1():
    gid_sum = 0
    for gid, games in process():
        if all(g.p1_valid for g in games):
            gid_sum += gid
    return gid_sum


def part_2():
    power_sum = 0
    for gid, games in process():
        maxes = Handful()
        for handful in games:
            maxes.set_max(handful)
        debug((gid, maxes))
        power_sum += maxes.power
    return power_sum
