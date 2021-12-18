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


# def reduce(vals):
#     brace_count = 0
#     for (n, c) in enumerate(vals):
#         if c == "[":
#             brace_count += 1
#             if brace_count >= 5:
#                 anchor = n
#                 # search left for a number to add to
#                 for i in range(n,-1,-1):


def part_1():
    for ipt in process():
        debug(ipt)
        # return process()
    return ""


def part_2():
    return process()
