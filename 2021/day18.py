import common
from common import debug
import settings


def process():
    input_data = common.read_string_file()
    for vals in input_data:
        debug(vals)
        ipt = []
        n = 0
        while n < len(vals):
            if vals[n] in ("[", "]"):
                ipt.append(vals[n])
                n += 1
            elif vals[n] == ",":
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


def reduce(vals):
    brace_count = 0
    explode = False
    for (n, c) in enumerate(vals):
        # debug((n, c, vals))
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
                for i in range(n + 2, len(vals)):
                    if type(vals[i]) is int:
                        vals[i] += vals[n + 1]
                        break
                vals[n - 1 : n + 3] = [0]


def part_1():
    for ipt in process():
        reduce(ipt)
        debug(ipt)
        # return process()
    return ""


def part_2():
    return process()
