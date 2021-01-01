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
        p = []
        if "|" in pattern:
            p.append("(")
        for c in pattern.split(" "):
            if c.strip():
                if c == "|":
                    p.append("|")
                elif c[0] in "0123456789":
                    p.append(f"{{r{c}}}")
                else:
                    p.append(c.strip('"'))
        if "|" in pattern:
            p.append(")")
        rules[f"r{r}"] = "".join(p)
    messages = [line for line in input_data]
    return (rules, messages)


def part_1():
    (rules, messages) = process()
    pattern = f"^{rules['r0']}$"
    while "{" in pattern:
        pattern = pattern.format(**rules)
    debug(pattern)
    pat = regex.compile(pattern)

    match_count = 0
    for msg in messages:
        m = bool(pat.match(msg))
        debug(f"{msg}: {m}")
        if m:
            match_count += 1

    return match_count


def part_2():
    (rules, messages) = process(
        {"8: 42": "8: 42 | 42 8", "11: 42 31": "11: 42 31 | 42 11 31"}
    )
    replacements = {"r8": "({r42})+?", "r11": "(<42_xxx>{r42})+({31_yyyr31})+?"}

    pattern = rules["r0"]
    for (r, rep) in replacements.items():
        rules[r] = rep

    while "{" in pattern:
        pattern = pattern.format(**rules)
    print(pattern)
    pat = regex.compile(pattern)

    match_count = 0
    for msg in messages:
        m = bool(pat.match(msg))
        debug(f"{msg}: {m}")
        if m:
            match_count += 1

    return match_count
