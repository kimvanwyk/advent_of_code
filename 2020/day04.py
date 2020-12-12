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


def process():
    passports = parse_lines()
    if settings.settings.debug:
        pprint.pprint(passports)
    return passports


def part_1():
    passports = process()
    return sum(
        [
            1
            for passport in passports
            if all(
                [
                    c in passport
                    for c in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
                ]
            )
        ]
    )


def part_2():
    return process()
