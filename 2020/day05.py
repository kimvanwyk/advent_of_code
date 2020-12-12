import common
import settings


def reduce_range(steps, initial_size, left, right):
    r = list(range(0, initial_size))
    for step in steps:
        if step == left:
            r = r[: len(r) // 2]
        elif step == right:
            r = r[len(r) // 2 :]
        else:
            raise ValueError(f"Invalid step data: {step} from {steps}")
    return r[0]


def find_row(steps):
    return reduce_range(steps, 128, "F", "B")


def find_col(steps):
    return reduce_range(steps, 8, "L", "R")


def process():
    sids = []
    input_data = common.read_string_file()
    for l in input_data:
        row = find_row(l[:7])
        col = find_col(l[7:])
        sid = (row * 8) + col
        sids.append(sid)
        if settings.settings.debug:
            print(row, col, sid)
    return sids


def part_1():
    sids = process()
    return max(sids)


def part_2():
    sids = process()
    sids.sort()
    for i in range(1, len(sids)):
        if sids[i] - sids[i - 1] > 1:
            print(i, sids[i - 1], sids[i], sids[i] - 1)
            return sids[i] - 1
    return ""
