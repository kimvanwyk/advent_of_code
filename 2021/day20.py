import common
from common import debug
import settings

from copy import deepcopy


def print_image(image_dict):
    keys = list(image_dict.keys())
    keys.sort(key=lambda x: x[0])
    xminmax = (keys[0][0], keys[-1][0] + 1)
    keys.sort(key=lambda x: x[1])
    yminmax = (keys[0][1], keys[-1][1] + 1)

    debug("")
    for y in range(*yminmax):
        line = []
        for x in range(*xminmax):
            if (x, y) in image_dict:
                line.append("#" if image_dict[(x, y)] else ".")
            else:
                line.append(" ")
        debug(" ".join(line))
    debug("")


def apply_algo(image_dict, algo, border=0):
    # Loop over current known coords
    # *  If a coord needs a calc from an unknown coord, add unknown coord to a list of new items
    # *  Assume value of unknown point is border val
    # *  Set val of known coord to a list of the values in order
    # Loop over list of new coords and insert into new dict:
    # *  Calc val of new coord:
    #    *  Use border for unknown coord
    #    *  Use middle val of known coord
    #    * Set bew dict key for new coord to algo lookup
    # Loop over all keys in image dict:
    # * Set val to algo lookup
    # Update image_dict with new dict
    # Return image dict

    current_dict = {}
    new_coords = []
    for (coord, val) in image_dict.items():
        val = []
        for (dx, dy) in (
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (0, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ):
            neighbour = (coord[0] + dx, coord[1] + dy)
            if neighbour not in image_dict:
                new_coords.append(neighbour)
                val.append(border)
            else:
                val.append(image_dict[neighbour])
        current_dict[coord] = val

    new_dict = {}
    for coord in new_coords:
        val = []
        for (dx, dy) in (
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (0, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ):
            neighbour = (coord[0] + dx, coord[1] + dy)
            if neighbour not in image_dict:
                val.append(border)
            else:
                val.append(image_dict[neighbour])
        new_dict[coord] = algo[int("".join([str(c) for c in val]), 2)]

    for (k, val) in current_dict.items():
        current_dict[k] = algo[int("".join([str(c) for c in val]), 2)]

    current_dict.update(new_dict)

    return current_dict


def process():
    input_data = list(common.read_string_file())
    algo = [1 if c == "#" else 0 for c in input_data[0]]
    # print((algo, len(algo)))

    # image starts on line 3
    image_dict = {}
    for (y, row) in enumerate(input_data[2:]):
        for (x, col) in enumerate(row):
            image_dict[(x, y)] = 1 if col == "#" else 0

    border = 0
    n = 0
    while n < 2:
        print_image(image_dict)
        image_dict = apply_algo(image_dict, algo, border=border)
        print_image(image_dict)
        if algo[0] == 1 and algo[-1] == 0:
            border = 1 if border == 0 else 0
        n += 1
    return sum(image_dict.values())


def part_1():
    return process()


def part_2():
    return process()
