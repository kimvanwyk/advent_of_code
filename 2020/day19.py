import regex

import common
from common import debug
import settings

LONGEST_LINE = 96


def process(mapping={}):
    rules = {}
    input_data = common.read_string_file()
    for line in input_data:
        if not line:
            break
        line = mapping.get(line, line)
        (r, pattern) = line.split(":")
        p = [[]]
        for c in pattern.split(" "):
            if c.strip():
                if c == "|":
                    p.append([])
                elif c[0] in "123456789":
                    p[-1].append(int(c))
                else:
                    p = c.strip('"')
        rules[int(r)] = p if type(p) is str else tuple(p)
    messages = [line for line in input_data]
    return (rules, messages)


# heavily influenced by https://github.com/mebeim/aoc/blob/master/2020/README.md#day-19---monster-messages
def match_message(rules, message, rule=0, index=0):
    if index >= len(message):
        return []

    debug(f"Rule Num: {rule}; index: {index}; rule: {rules[rule]}; message: {message}")
    rule = rules[rule]
    # if rule is a string and it matches, return next index as this match is done
    if type(rule) is str:
        if message[index] == rule:
            return [index + 1]
        return []

    hits = []
    for ruleset in rule:
        ruleset_hits = [index]

        for sub_rule in ruleset:
            new_hits = []
            for idx in ruleset_hits:
                new_hits += match_message(rules, message, sub_rule, idx)
            ruleset_hits = new_hits

        hits += ruleset_hits
    return hits


def part_1():
    (rules, messages) = process()
    match_count = 0
    for message in messages:
        matches = match_message(rules, message)
        match_count += any(len(message) == m for m in matches)

    return match_count


def part_2():
    (rules, messages) = process(
        {"8: 42": "8: 42 | 42 8", "11: 42 31": "11: 42 31 | 42 11 31"}
    )

    rules["r8"] = "({r42})+"
    run = []
    for n in range(1, LONGEST_LINE + 1):
        run.append(f"(({{r42}}[{n}])({{r31}}[{n}]))")
    rules["r11"] = f"({'|'.join(run)})"

    pattern = rules["r0"]
    while "{" in pattern:
        pattern = pattern.format(**rules)
    pattern = pattern.replace("[", "{").replace("]", "}")
    # print(pattern)
    pat = regex.compile(pattern)

    match_count = 0
    for msg in messages:
        m = bool(pat.match(msg))
        debug(f"{msg}: {m}")
        if m:
            match_count += 1

    return match_count
