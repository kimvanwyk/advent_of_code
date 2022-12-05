import common
from common import debug
import settings

from collections import namedtuple
import re

MOVE = namedtuple("Move", "move src target")
move_pattern = re.compile("move (\d+) from (\d+) to (\d+)")


def read():
    with open(settings.settings.input_file, "r") as fh:
        for line in fh.readlines():
            yield line


def process():
    stacks = {}
    # input crate lines are all the same length, no fancy parsing needed
    with open(settings.settings.input_file, "r") as fh:
        for line in fh.readlines():
            indices = list(range(1, len(line), 4))
            for i in range(1, (len(line) // 4) + 1):
                stacks[i] = []
            break
    debug(f"{indices=}")

    for line in read():
        if not line.strip() or ((len(line) >= 2) and line[1] == "1"):
            break
        for (i, idx) in enumerate(indices, 1):
            if line[idx].strip():
                stacks[i].append(line[idx])
    for k in stacks:
        stacks[k].reverse()
    debug(stacks)

    moves = []
    for line in read():
        if "move" in line:
            moves.append(
                MOVE(*[int(g) for g in move_pattern.match(line.strip()).groups()])
            )
    debug(moves)
    return (stacks, moves)


def part_1():
    (stacks, moves) = process()
    for move in moves:
        for x in range(move.move):
            stacks[move.target].append(stacks[move.src].pop(-1))
    debug(stacks)
    return "".join([stack[-1] for stack in stacks.values()])


def part_2():
    return process()
