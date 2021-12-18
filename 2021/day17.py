import common
from common import debug
import settings


class Probe:
    def __init__(self, xlims, ylims):
        self.xlims = xlims
        self.ylims = ylims
        self.maxy = None

    def test_path(self, xd, yd):
        (x, y) = (0, 0)
        self.highest = 0
        result = False
        while True:
            x += xd
            y += yd
            if y > self.highest:
                self.highest = y
            if xd > 0:
                xd -= 1
            elif xd < 0:
                xd += 1
            yd -= 1
            if (y < self.ylims[1]) or (x < self.xlims[0] and y < self.ylims[0]):
                break
            if (self.xlims[0] <= x <= self.xlims[1]) and (
                self.ylims[0] >= y >= self.ylims[1]
            ):
                result = True
                if self.maxy and self.highest > self.maxy:
                    self.maxy = self.highest
                break
        return result


def process():
    rets = []
    for s in next(common.read_string_file()).split(", "):
        rets.extend([int(c.strip()) for c in s[2:].split("..")])
    return rets


def part_1():
    (minx, maxx, miny, maxy) = process()
    xlims = [minx, maxx]
    xlims.sort()
    ylims = [miny, maxy]
    ylims.sort(reverse=True)
    debug((xlims, ylims))
    probe = Probe(xlims, ylims)

    for ipt in ((7, 2), (6, 3), (9, 0), (6, 9), (17, -4)):
        if probe.test_path(*(ipt)):
            debug(f"Success with {ipt}")
            debug(probe.highest)
        else:
            debug(f"Failure with {ipt}")
    return ""


def part_2():
    return process()
