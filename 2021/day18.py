import common
from common import debug
import settings


def process():
    input_data = common.read_string_file()
    for vals in input_data:
        if vals[0] != "#":
            # debug(vals)
            ipt = []
            n = 0
            while n < len(vals):
                if vals[n] in ("[", "]", ","):
                    ipt.append(vals[n])
                    n += 1
                else:
                    num = []
                    for i in range(n, len(vals)):
                        if vals[i] in "0123456789":
                            num.append(vals[i])
                        else:
                            break
                    if num:
                        ipt.append(int("".join(num)))
                    n = i
            yield ipt


def addition(vals, addor):
    vals.insert(0, "[")
    vals.append(",")
    vals.extend(addor)
    vals.append("]")


def reduce(vals):
    while True:
        acted = False
        brace_count = 0
        for (n, c) in enumerate(vals):
            if c == "[":
                brace_count += 1
            elif c == "]":
                brace_count -= 1
            elif type(c) is int:
                if brace_count >= 5:
                    acted = True
                    anchor = n
                    # search left for a number to add to
                    for i in range(n - 1, -1, -1):
                        if type(vals[i]) is int:
                            vals[i] += vals[n]
                            break
                    for i in range(n + 3, len(vals)):
                        if type(vals[i]) is int:
                            vals[i] += vals[n + 2]
                            break
                    vals[n - 1 : n + 4] = [0]
                    # debug(("explode", n, c, "".join([str(c) for c in vals])))
                    break

        if not acted:
            for (n, c) in enumerate(vals):
                if (type(c) is int) and (c >= 10):
                    acted = True
                    vals[n : n + 1] = ["[", c // 2, ",", (c // 2) + (c % 2), "]"]
                    # debug(("split", n, c, "".join([str(v) for v in vals])))
                    break

        if not acted:
            break


def magnitude(vals):
    while len(vals) > 1:
        for n in range(len(vals)):
            if vals[n] == "]":
                # debug((vals, n, vals[n - 4 :]))
                vals[n - 4 : n + 1] = [vals[n - 3] * 3 + vals[n - 1] * 2]
                break
    return vals[0]


def part_1():
    if 0:
        # usewith parts 1 - 3
        ipt = None
        for addee in process():
            if ipt is None:
                ipt = addee
            else:
                addition(ipt, addee)
                # debug(f'addition:  {"".join([str(c) for c in ipt])}')
                reduce(ipt)
                # debug(f'reduction:  {"".join([str(c) for c in ipt])}')
                # debug("")
                # break
        debug("".join([str(c) for c in ipt]))
        debug("")
    if 0:
        # use wth part 4
        for ipt in process():
            debug(ipt)
            debug(magnitude(ipt[:]))
    if 1:
        # use with p5 and prod
        ipt = None
        for addee in process():
            if ipt is None:
                ipt = addee
            else:
                addition(ipt, addee)
                reduce(ipt)
        debug(("sum", "".join([str(c) for c in ipt])))
        magn = magnitude(ipt)
        debug(("magn", magn))
    return magn


def part_2():
    return process()
