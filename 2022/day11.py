import common
from common import debug
import settings


from attr import define, field

# from gmpy2 import mpz

import operator
import os

OPERATORS = {"*": operator.mul, "+": operator.add}
ITEM_LENGTHS = {}


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, "big")


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, "big")


@define(slots=False)
class Monkey:
    key: int
    operator: type(operator.add)
    operand: int
    test: int
    throwees: []
    reduce_worry: bool
    inspections: int = field(init=False)

    def __attrs_post_init__(self):
        self.inspections = 0

    def process(self):
        for n in range(1, ITEM_LENGTHS[self.key] + 1):
            flocal = f"items_{self.key:02}_{n:05}.bin"
            with open(flocal, "rb") as fh:
                self.inspections += 1
                item = int_from_bytes(bytes(fh.read()))
                item = self.operator(
                    item, self.operand if self.operand is not None else item
                )
                if self.reduce_worry:
                    item = item // 3
                other = self.throwees[item % self.test == 0]
                ITEM_LENGTHS[other] += 1
                with open(
                    f"items_{other:02}_{ITEM_LENGTHS[other]:05}.bin", "wb"
                ) as fout:
                    fout.write(int_to_bytes(item))
            os.remove(flocal)
        ITEM_LENGTHS[self.key] = 0


def process(reduce_worry):
    input_data = common.read_string_file()
    monkeys = {}
    kargs = {"reduce_worry": reduce_worry}
    for line in input_data:
        if "Monkey" in line:
            kargs["key"] = int(line.split(" ")[-1][:-1])
        if "Starting" in line:
            length = 0
            for item in line.split(":")[-1].split(", "):
                length += 1
                with open(f"items_{kargs['key']:02}_{length:05}.bin", "wb") as fh:
                    fh.write(int_to_bytes(int(item)))
            ITEM_LENGTHS[kargs["key"]] = length
        if "Operation" in line:
            (operator, operand) = line.split("old ")[-1].split(" ")
            kargs["operator"] = OPERATORS[operator]
            try:
                kargs["operand"] = int(operand)
            except Exception as e:
                kargs["operand"] = None
        if "Test" in line:
            kargs["test"] = int(line.split("by ")[-1])
        if "If true" in line:
            kargs["throwees"] = {True: int(line.split("monkey ")[-1])}
        if "If false" in line:
            kargs["throwees"][False] = int(line.split("monkey ")[-1])
            monkeys[kargs["key"]] = Monkey(**kargs)
    return monkeys


def process_monkeys(monkeys, rounds):
    round = 0
    while round < rounds:
        for monkey in monkeys.values():
            monkey.process()
        # debug(f"{round=}  {monkeys=}")
        round += 1
    return monkeys


def part_1():
    monkeys = process(reduce_worry=True)
    monkeys = process_monkeys(monkeys, 20)
    inspections = [m.inspections for m in monkeys.values()]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


def part_2():
    monkeys = process(reduce_worry=False)
    monkeys = process_monkeys(monkeys, 10000)
    inspections = [m.inspections for m in monkeys.values()]
    inspections.sort(reverse=True)
    debug(inspections[:3])
    return inspections[0] * inspections[1]
