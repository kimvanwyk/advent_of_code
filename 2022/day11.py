import common
from common import debug
import settings


from attr import define, field
import operator

OPERATORS = {"*": operator.mul, "+": operator.add}


@define(slots=False)
class Monkey:
    items: []
    operator: type(operator.add)
    operand: int
    test: int
    throwees: []
    inspections: int = field(init=False)

    def __attrs_post_init__(self):
        self.inspections = 0

    def process(self):
        actions = []
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            item = self.operator(
                item, self.operand if self.operand is not None else item
            )
            item = item // 3
            actions.append((item, self.throwees[item % self.test == 0]))
        return actions


def process():
    input_data = common.read_string_file()
    monkeys = {}
    kargs = {}
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
    debug(monkeys)
    return monkeys


def part_1():
    monkeys = process()
    for round in range(20):
        for monkey in monkeys.values():
            actions = monkey.process()
            debug(f"{actions=}")
            for action in actions:
                monkeys[action[1]].items.append(action[0])
        debug(monkeys)
    inspections = [m.inspections for m in monkeys.values()]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


def part_2():
    return process()
