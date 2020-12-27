import re

import common
from common import debug
import settings


print(
    '{"r0": "{r4}{r1}{r5}", "r1": "({r2}{r3}|{r3}{r2})", "r2": "({r4}{r4}|{r5}{r5})", "r3": "({r4}{r5}|{r5}{r4})", "r4":"a", "r5":"b"}'
)


def process():
    rules = {}
    input_data = common.read_string_file()
    for line in input_data:
        if not line:
            break
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
    pat = re.compile(pattern)

    match_count = 0
    for msg in messages:
        m = bool(pat.match(msg))
        debug(f"{msg}: {m}")
        if m:
            match_count += 1

    return match_count


def part_2():
    return process()
