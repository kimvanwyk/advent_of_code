import common
from common import debug
import settings

import numpy as np


def process(find_last=False):
    def print_boards():
        if settings.settings.debug:
            for row in range(boards[0].shape[0]):
                debug(
                    "   ".join(
                        [
                            " ".join([f"{i: 3}" for i in board[row, :].tolist()])
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
                boards.append(np.array(vals, dtype=np.int16))
            vals = []
        else:
            vals.append([l for l in line.split(" ") if l])

    print_boards()
    for input_val in inputs:
        debug(f"{input_val=}")
        board_index = -1
        for board in boards[:]:
            win = False
            board_index += 1
            idx = np.argwhere(board == input_val)
            debug(f"{idx=} {board_index=}")
            if tuple(idx):
                if board[tuple(idx[0])] > 0:
                    board[tuple(idx[0])] *= -1
                else:
                    board[tuple(idx[0])] = -1

            for row in range(board.shape[0]):
                if board[row : row + 1, :].max() <= -1:
                    win = True
                    break
            else:
                for col in range(board.shape[1]):
                    if board[:, col : col + 1].max() <= -1:
                        win = True
                        break
            if win:
                if not find_last:
                    print_boards()
                    total = board[board >= 0].sum()
                    debug(f"{total=}  {input_val=}")
                    return int(total * input_val)
                else:
                    if len(boards) == 1:
                        print_boards()
                        total = board[board >= 0].sum()
                        debug(f"{total=}  {input_val=}")
                        return int(total * input_val)
                    boards.pop(board_index)
        print_boards()


def part_1():
    return process()


def part_2():
    return process(find_last=True)
