from collections import defaultdict
import common
from common import debug
import settings

import string

import networkx as nx


def process():
    input_data = common.read_string_file()
    G = nx.Graph()
    G.add_edges_from([l.split("-") for l in input_data])
    return G


class NodeProcessor:
    def __init__(self, graph, allow_double=False):
        self.graph = graph
        self.total_paths = 0
        self.allow_double = allow_double
        self.paths = []

    def process(self, node, path, seen_double=False):
        proceed = False
        for neighbour in self.graph.neighbors(node):
            # debug(f"{node=}  {neighbour=}")
            if neighbour == "end":
                debug(f"Good path: {path}")
                if settings.settings.debug:
                    self.paths.append(path)
                self.total_paths += 1
                continue
            elif neighbour == "start":
                continue
            elif all(n in string.ascii_lowercase for n in neighbour):
                if neighbour in path:
                    if not self.allow_double:
                        continue
                    else:
                        if not seen_double:
                            seen_double = True
                            proceed = True
                            continue
                else:
                    proceed = True
            else:
                proceed = True
            if proceed:
                if (not path) or path[-1] != node:
                    path.append(node)
                self.process(neighbour, path[:], seen_double)


def part_1():
    graph = process()
    np = NodeProcessor(graph, allow_double=False)
    np.process("start", [])
    return np.total_paths


def part_2():
    graph = process()
    np = NodeProcessor(graph, allow_double=True)
    np.process("start", [])
    np.paths.sort()
    debug(np.paths)
    return np.total_paths
