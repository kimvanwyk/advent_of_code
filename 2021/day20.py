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


def expand_image(image):
    """Return a new image with 2 rows of dark pixels at the top and bottom and 2 dark pixels on either side of each row"""
    out_image = []
    row_len = len(image[0]) + 4
    out_image.append([0] * row_len)
    out_image.append([0] * row_len)
    for row in image:
        l = [0, 0]
        l.extend(row)
        l.extend([0, 0])
        out_image.append(l)
    out_image.append([0] * row_len)
    out_image.append([0] * row_len)
    return out_image


def process():
    input_data = list(common.read_string_file())
    algo = [1 if c == "#" else 0 for c in input_data[0]]
    # debug((algo, len(algo)))

    # image starts on line 3
    image = []
    for row in input_data[2:]:
        image.append([1 if c == "#" else 0 for c in row])
    image = expand_image(image)
    print_image(image)
    image = apply_algo(image, algo)
    print_image(image)
    return ""


def part_1():
    return process()


def part_2():
    return process()
