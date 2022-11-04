import common
from common import debug
import settings

from copy import deepcopy


def print_image(image):
    for row in image:
        debug(" ".join(["#" if c else "." for c in row]))


def apply_algo(image, algo):
    out_image = deepcopy(image)
    for row in range(1, len(image) - 1):
        for col in range(1, len(image[0]) - 1):
            val = "".join(
                [
                    str(c)
                    for c in [
                        image[row - 1][col - 1],
                        image[row - 1][col],
                        image[row - 1][col + 1],
                        image[row][col - 1],
                        image[row][col],
                        image[row][col + 1],
                        image[row + 1][col - 1],
                        image[row + 1][col],
                        image[row + 1][col + 1],
                    ]
                ]
            )
            print(row, col, val, int(val, 2))
            out_image[row][col] = algo[int(val, 2)]
    return out_image


def process():
    input_data = list(common.read_string_file())
    algo = [1 if c == "#" else 0 for c in input_data[0]]
    # debug((algo, len(algo)))

    # image starts on line 3
    # add 2 dark pixels to each side of each row and 2 rows of zeroes on the top and bottom
    row_len = len(input_data[2]) + 4
    image = [[0] * row_len, [0] * row_len]
    for row in input_data[2:]:
        l = [0, 0]
        l.extend([1 if c == "#" else 0 for c in row])
        l.extend([0, 0])
        image.append(l)
    image.append([0] * row_len)
    image.append([0] * row_len)
    print_image(image)
    out_image = apply_algo(image, algo)
    print_image(out_image)
    return ""


def part_1():
    return process()


def part_2():
    return process()
