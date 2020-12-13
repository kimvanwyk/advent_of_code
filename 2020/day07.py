from collections import defaultdict
from pprint import pprint


import common
import settings


def process():
    bags_top_down = {}
    bags_bottom_up = defaultdict(list)
    input_data = common.read_string_file()
    for line in input_data:
        (front, content_string) = line.split("contain")
        bag = front.split("bag")[0].strip()
        if "no other bags" in content_string:
            bags_top_down[bag] = None
        else:
            d = {}
            for content in content_string.split(","):
                (num, description) = content.strip().split(" ", 1)
                desc = description.strip().rsplit(" ", 1)[0].strip()
                d[desc] = int(num.strip())
                bags_bottom_up[desc].append(bag)
            bags_top_down[bag] = d
    if settings.settings.debug:
        pprint(bags_top_down)
        pprint(bags_bottom_up)

    return (bags_top_down, bags_bottom_up)


# recursion refresher via https://stackoverflow.com/questions/8991840/recursion-using-yield
def part_1(own_bag="shiny gold"):
    options = []
    (bags_top_down, bags_bottom_up) = process()

    def record_bag(bag):
        if bag != own_bag:
            options.append(bag)

    def recurse_bags(bag):
        record_bag(bag)
        for child in bags_bottom_up[bag]:
            recurse_bags(child)

    recurse_bags(own_bag)
    s = set(options)
    if settings.settings.debug:
        print(options)
        print(s)
        print(len(s))
    return len(s)


def part_2():
    return process()
