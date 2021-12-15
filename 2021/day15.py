import common
from common import debug
import settings

import networkx as nx


class Graph:
    def __init__(self, repeats):
        input_data = common.read_string_file()
        self.graph = nx.Graph()
        self.maxx = 0
        self.maxy = 0
        vals = {}
        for ymult in range(repeats):
            input_data = common.read_string_file()
            for (y, line) in enumerate(input_data):
                if line:
                    for xmult in range(repeats):
                        for (x, v) in enumerate(line):
                            v = int(v)
                            v += ymult
                            if v > 9:
                                v -= 9
                            v += xmult
                            if v > 9:
                                v -= 9
                            self.graph.add_node(
                                (
                                    x + ((self.maxx + 1) * xmult),
                                    y + ((self.maxy + 1) * ymult),
                                ),
                                weight=v,
                            )
                        if xmult == 0:
                            self.maxx = x
            if ymult == 0:
                self.maxy = y
        self.maxx = ((self.maxx + 1) * repeats) - 1
        self.maxy = ((self.maxy + 1) * repeats) - 1
        debug(self.maxx)
        debug(self.maxy)
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
        # debug(path)
        total = sum(self.graph.nodes[pos].get("weight", 0) for pos in path[1:])
        debug(total)
        return total


def part_1():
    graph = Graph(1)
    return graph.cheapest_path()


def part_2():
    graph = Graph(5)
    return graph.cheapest_path()
