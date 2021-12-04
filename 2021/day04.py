import common
from common import debug
import settings

import numpy as np


class Board:
    def __init__(self, data):
        self.winning = False
        self.board = np.array(data, dtype=np.int16)

    def set_val(self, input_val):
        idx = np.argwhere(self.board == input_val)
        debug(f"{idx=}")
        if tuple(idx):
            if self.board[tuple(idx[0])] > 0:
                self.board[tuple(idx[0])] *= -1
            else:
                self.board[tuple(idx[0])] = -1

    def check_for_win(self):
        for row in range(self.board.shape[0]):
            if self.board[row : row + 1, :].max() <= -1:
                self.winning = True
                break
        else:
            for col in range(self.board.shape[1]):
                if self.board[:, col : col + 1].max() <= -1:
                    self.winning = True
                    break
        return self.winning

    def score(self, input_val):
        total = self.board[self.board >= 0].sum()
        debug(f"{total=}  {input_val=}")
        return int(total * input_val)


def process(find_last=False):
    def print_boards():
        if settings.settings.debug:
            for row in range(boards[0].board.shape[0]):
                debug(
                    "   ".join(
                        [
                            " ".join([f"{i: 3}" for i in board.board[row, :].tolist()])
                            for board in boards
                        ]
                    )
                )

    input_data = common.read_string_file()
    inputs = [int(i) for i in next(input_data).split(",")]
    debug(inputs)

    boards = []
    vals = []
    for line in input_data:
        if not line:
            if vals:
                boards.append(Board(vals))
            vals = []
        else:
            vals.append([l for l in line.split(" ") if l])

    remaining_boards = len(boards)
    print_boards()
    for input_val in inputs:
        debug(f"{input_val=}")
        for board in boards:
            if not board.winning:
                board.set_val(input_val)
                if board.check_for_win():
                    if not find_last:
                        print_boards()
                        return board.score(input_val)
                    else:
                        remaining_boards -= 1
                        if not remaining_boards:
                            print_boards()
                            return board.score(input_val)
        print_boards()


def part_1():
    return process()


def part_2():
    return process(find_last=True)
