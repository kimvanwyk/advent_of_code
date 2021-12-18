import common
from common import debug
import settings

P2_MATCHES = set(
    (
        (23, -10),
        (25, -9),
        (27, -5),
        (29, -6),
        (22, -6),
        (21, -7),
        (9, 0),
        (27, -7),
        (24, -5),
        (25, -7),
        (26, -6),
        (25, -5),
        (6, 8),
        (11, -2),
        (20, -5),
        (29, -10),
        (6, 3),
        (28, -7),
        (8, 0),
        (30, -6),
        (29, -8),
        (20, -10),
        (6, 7),
        (6, 4),
        (6, 1),
        (14, -4),
        (21, -6),
        (26, -10),
        (7, -1),
        (7, 7),
        (8, -1),
        (21, -9),
        (6, 2),
        (20, -7),
        (30, -10),
        (14, -3),
        (20, -8),
        (13, -2),
        (7, 3),
        (28, -8),
        (29, -9),
        (15, -3),
        (22, -5),
        (26, -8),
        (25, -8),
        (25, -6),
        (15, -4),
        (9, -2),
        (15, -2),
        (12, -2),
        (28, -9),
        (12, -3),
        (24, -6),
        (23, -7),
        (25, -10),
        (7, 8),
        (11, -3),
        (26, -7),
        (7, 1),
        (23, -9),
        (6, 0),
        (22, -10),
        (27, -6),
        (8, 1),
        (22, -8),
        (13, -4),
        (7, 6),
        (28, -6),
        (11, -4),
        (12, -4),
        (26, -9),
        (7, 4),
        (24, -10),
        (23, -8),
        (30, -8),
        (7, 0),
        (9, -1),
        (10, -1),
        (26, -5),
        (22, -9),
        (6, 5),
        (7, 5),
        (23, -6),
        (28, -10),
        (10, -2),
        (11, -1),
        (20, -9),
        (14, -2),
        (29, -7),
        (13, -3),
        (23, -5),
        (24, -8),
        (27, -9),
        (30, -7),
        (28, -5),
        (21, -10),
        (7, 9),
        (6, 6),
        (21, -5),
        (27, -10),
        (7, 2),
        (30, -9),
        (21, -8),
        (22, -7),
        (24, -9),
        (20, -6),
        (6, 9),
        (29, -5),
        (8, -2),
        (27, -8),
        (30, -5),
        (24, -7),
    )
)


class Probe:
    def __init__(self, xlims, ylims):
        self.xlims = xlims
        self.ylims = ylims
        self.maxy = None
        self.good_paths = []

    def test_path(self, xd, yd):
        path = (xd, yd)
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
            # if path == (7, -1):
            #     print(
            #         path,
            #         (x, y),
            #         self.xlims,
            #         self.ylims,
            #         y < self.ylims[1],
            #         (self.xlims[0] <= x <= self.xlims[1])
            #         and (self.ylims[0] >= y >= self.ylims[1]),
            #     )

            if y < self.ylims[1]:
                break
            if (self.xlims[0] <= x <= self.xlims[1]) and (
                self.ylims[0] >= y >= self.ylims[1]
            ):
                result = True
                if (self.maxy is None) or self.highest > self.maxy:
                    self.maxy = self.highest
                    debug(f"New max: {self.maxy=}")
                debug(f"{path=}")
                self.good_paths.append(path)
                break
        return result


def process():
    rets = []
    for s in next(common.read_string_file()).split(", "):
        rets.extend([int(c.strip()) for c in s[2:].split("..")])
    return rets


def part_1_known_paths(probe):

    for ipt in ((7, 2), (6, 3), (9, 0), (6, 9), (17, -4)):
        if probe.test_path(*(ipt)):
            debug(f"Success with {ipt}")
            debug(probe.highest)
        else:
            debug(f"Failure with {ipt}")


def get_probe():
    (minx, maxx, miny, maxy) = process()
    xlims = [minx, maxx]
    xlims.sort()
    ylims = [miny, maxy]
    ylims.sort(reverse=True)
    debug((xlims, ylims))
    return Probe(xlims, ylims)


def process_paths(probe):
    for xd in range(1, probe.xlims[1] * 4):
        for yd in range(probe.ylims[1], probe.xlims[1] * 4):
            probe.test_path(xd, yd)


def part_1():
    probe = get_probe()
    process_paths(probe)
    return probe.maxy


def part_2():
    probe = get_probe()
    process_paths(probe)
    return len(probe.good_paths)
