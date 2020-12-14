from collections import defaultdict
from pprint import pprint

import attr

import common
from common import debug
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
    debug(bags_top_down, pretty=True)
    debug(bags_bottom_up, pretty=True)

    return (bags_top_down, bags_bottom_up)


@attr.s
class Nodes:
    bag_dict = attr.ib()
    nodes = attr.ib(default=attr.Factory(dict))

    def add_node(self, bag):
        if bag not in self.nodes:
            if self.bag_dict[bag] is None:
                self.nodes[bag] = None
            else:
                self.nodes[bag] = []
                for (k, v) in self.bag_dict[bag].items():
                    for n in range(v):
                        self.add_node(k)
                        if self.nodes[k]:
                            self.nodes[bag].append(k)
                            self.nodes[bag].extend(self.nodes[k])
                            debug(f"{bag}: extend {self.nodes[k]}")
                        else:
                            self.nodes[bag].append(k)
                            debug(f"{bag}: append {k}")


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
    debug(options)
    debug(s)
    debug(len(s))
    return len(s)


def part_2(own_bag="shiny gold"):
    (bags_top_down, bags_bottom_up) = process()
    nodes = Nodes(bags_top_down)
    nodes.add_node(own_bag)
    print(len(nodes.nodes[own_bag]))
    return len(nodes.nodes[own_bag])
