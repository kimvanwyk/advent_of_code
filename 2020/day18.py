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


def calculate_parenthesis_add_first(instructions):
    debug(f"Parenthesis instructions: {instructions}")
    first = (add,)
    results = []
    n = 0
    while True:
        inst = instructions[n]
        if inst not in first:
            results.append(inst)
            n += 1
        else:
            results[-1] = inst(results[-1], instructions[n + 1])
            n += 2
        if n >= len(instructions):
            break

    result = results[0]
    if len(results) > 1:
        n = 1
        while True:
            result = results[n](result, results[n + 1])
            n += 2
            if n >= len(results):
                break

    return result


def process_algo(
    instructions,
    ops={"+": add, "*": mul},
    calculate_parenthesis_func=calculate_parenthesis,
):
    stack = [[]]
    debug(f"Algo instructions: {instructions}")
    for inst in instructions:
        debug(f"Stack: {stack}")
        if inst in ops:
            stack[-1].append(ops[inst])
        elif inst == "(":
            stack.append([])
        elif inst == ")":
            result = calculate_parenthesis_func(stack[-1])
            del stack[-1]
            stack[-1].append(result)
        else:
            stack[-1].append(int(inst))
    debug(f"Stack before final calc: {stack}")
    res = calculate_parenthesis_func(stack[-1])
    debug(f"Final result: {res}")
    return res


def process(calculate_parenthesis_func):
    results = []
    input_data = common.read_string_file()
    for line in input_data:
        result = process_algo(
            [c.strip() for c in line if c.strip()],
            calculate_parenthesis_func=calculate_parenthesis_func,
        )
        results.append(result)
    return results


def part_1():
    results = process(calculate_parenthesis)
    return sum(results)


def part_2():
    results = process(calculate_parenthesis_add_first)
    debug(results)
    return sum(results)
