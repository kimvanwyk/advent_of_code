import common
from common import debug
import settings


from attr import define, field

import array
import operator

OPERATORS = {"*": operator.mul, "+": operator.add}


@define(slots=False)
class Monkey:
    items: None
    operator: type(operator.add)
    operand: int
    test: int
    throwees: []
    reduce_worry: bool
    inspections: int = field(init=False)

    def __attrs_post_init__(self):
        self.inspections = 0

    def process(self):
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            item = self.operator(
                item, self.operand if self.operand is not None else item
            )
            if self.reduce_worry:
                item = item // 3
            yield (item, self.throwees[item % self.test == 0])


def process(reduce_worry):
    input_data = common.read_string_file()
    monkeys = {}
    kargs = {"reduce_worry": reduce_worry}
    for line in input_data:
        if "Monkey" in line:
            key = int(line.split(" ")[-1][:-1])
        if "Starting" in line:
            kargs["items"] = [int(item) for item in line.split(":")[-1].split(", ")]
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
            monkeys[key] = Monkey(**kargs)
    return monkeys


def process_monkeys(monkeys, rounds):
    round = 0
    while round < rounds:
        for monkey in monkeys.values():
            for action in monkey.process():
                monkeys[action[1]].items.append(action[0])
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
    monkeys = process_monkeys(monkeys, 800)
    inspections = [m.inspections for m in monkeys.values()]
    inspections.sort(reverse=True)
    debug(inspections[:3])
    return inspections[0] * inspections[1]
