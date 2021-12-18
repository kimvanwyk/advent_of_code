import common
from common import debug
import settings


def process():
    input_data = common.read_string_file()
    for vals in input_data:
        if vals[0] != "#":
            debug(vals)
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
        explode = False
        split = False
        brace_count = 0
        for (n, c) in enumerate(vals):
            if c == "[":
                brace_count += 1
            elif c == "]":
                brace_count -= 1
            elif type(c) is int:
                if (brace_count >= 5) and not explode:
                    explode = True
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
                    debug(("explode", n, c, "".join([str(c) for c in vals])))
                    break

                if c >= 10 and not split:
                    split = True
                    vals[n : n + 1] = ["[", c // 2, ",", (c // 2) + (c % 2), "]"]
                    debug(("split", n, c, "".join([str(v) for v in vals])))
                    break

        if not any((explode, split)):
            break


def part_1():
    for ipt in process():
        addition(ipt, ["[", 1, ",", 1, "]"])
        debug("".join([str(c) for c in ipt]))
        reduce(ipt)
        debug("".join([str(c) for c in ipt]))
        debug("")
        # return process()
    return ""


def part_2():
    return process()
