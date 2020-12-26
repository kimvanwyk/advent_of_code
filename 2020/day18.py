from operator import add, mul

import common
from common import debug
import settings


def calculate_parenthesis(instructions):
    debug(f"Parenthesis instructions: {instructions}")
    result = instructions[1](instructions[0], instructions[2])
    n = 3
    while n < len(instructions):
        debug(f"Parenthesis calc step: {n:02}: {result}")
        result = instructions[n](result, instructions[n + 1])
        n += 2
    debug(f"Parenthesis result: {result}")
    return result


def process_algo(instructions, ops={"+": add, "*": mul}):
    stack = [[]]
    debug(f"Algo instructions: {instructions}")
    for inst in instructions:
        debug(f"Stack: {stack}")
        if inst in ops:
            stack[-1].append(ops[inst])
        elif inst == "(":
            stack.append([])
        elif inst == ")":
            result = calculate_parenthesis(stack[-1])
            del stack[-1]
            stack[-1].append(result)
        else:
            stack[-1].append(int(inst))
    debug(f"Stack before final calc: {stack}")
    return calculate_parenthesis(stack[-1])


def process():
    input_data = common.read_string_file()
    for line in input_data:
        yield [c.strip() for c in line if c.strip()]


def part_1():
    results = []
    for instructions in process():
        result = process_algo(instructions)
        results.append(result)
    return sum(results)


def part_2():
    return process()
