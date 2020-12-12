import pprint

import attr

import common
import settings


def parse_lines():
    passports = []

    def add_passport_dict(items):
        passports.append(dict([item.split(":") for item in items]))

    items = []
    for line in common.read_string_file():
        if line:
            items.extend([l.strip() for l in line.split(" ")])
        else:
            add_passport_dict(items)
            items = []
    if items:
        add_passport_dict(items)
    return passports


def check_passport_part1(passport):
    return all(
        [c in passport for c in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")]
    )


def process(check):
    passports = parse_lines()
    if settings.settings.debug:
        pprint.pprint(passports)
    valids = 0
    for passport in passports:
        if check(passport):
            valids += 1
    return valids


def part_1():
    return process(check_passport_part1)


def part_2():
    return process()
