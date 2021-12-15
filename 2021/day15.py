import common
from common import debug
import settings

import networkx as nx


class Graph:
    def __init__(self):
        input_data = common.read_string_file()
        self.graph = nx.Graph()
        for (y, line) in enumerate(input_data):
            if line:
                for (x, v) in enumerate(line):
                    self.graph.add_node((x, y), weight=int(v))
            self.maxx = x
        self.maxy = y
        for x in range(self.maxx + 1):
            for y in range(self.maxy + 1):
                for (xd, yd) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if (x + xd >= 0) and (y + yd >= 0):
                        self.graph.add_edge((x, y), (x + xd, y + yd))

    def cheapest_path(self):
        path = nx.dijkstra_path(
            self.graph,
            (0, 0),
            (self.maxx, self.maxy),
            lambda u, v, e: self.graph.nodes[v].get("weight", 0),
        )
        debug(path)
        total = sum(self.graph.nodes[pos].get("weight", 0) for pos in path[1:])
        debug(total)
        return total


def part_1():
    graph = Graph()
    return graph.cheapest_path()


def part_2():
    return process()
