from collections import defaultdict
import common
from common import debug
import settings

import string

import networkx as nx

P2_T1_EXPECTED = (
    ("start", "A", "b", "A", "b", "A", "c", "A"),
    ("start", "A", "b", "A", "b", "A"),
    ("start", "A", "b", "A", "b"),
    ("start", "A", "b", "A", "c", "A", "b", "A"),
    ("start", "A", "b", "A", "c", "A", "b"),
    ("start", "A", "b", "A", "c", "A", "c", "A"),
    ("start", "A", "b", "A", "c", "A"),
    ("start", "A", "b", "A"),
    ("start", "A", "b", "d", "b", "A", "c", "A"),
    ("start", "A", "b", "d", "b", "A"),
    ("start", "A", "b", "d", "b"),
    ("start", "A", "b"),
    ("start", "A", "c", "A", "b", "A", "b", "A"),
    ("start", "A", "c", "A", "b", "A", "b"),
    ("start", "A", "c", "A", "b", "A", "c", "A"),
    ("start", "A", "c", "A", "b", "A"),
    ("start", "A", "c", "A", "b", "d", "b", "A"),
    ("start", "A", "c", "A", "b", "d", "b"),
    ("start", "A", "c", "A", "b"),
    ("start", "A", "c", "A", "c", "A", "b", "A"),
    ("start", "A", "c", "A", "c", "A", "b"),
    ("start", "A", "c", "A", "c", "A"),
    ("start", "A", "c", "A"),
    ("start", "A"),
    ("start", "b", "A", "b", "A", "c", "A"),
    ("start", "b", "A", "b", "A"),
    ("start", "b", "A", "b"),
    ("start", "b", "A", "c", "A", "b", "A"),
    ("start", "b", "A", "c", "A", "b"),
    ("start", "b", "A", "c", "A", "c", "A"),
    ("start", "b", "A", "c", "A"),
    ("start", "b", "A"),
    ("start", "b", "d", "b", "A", "c", "A"),
    ("start", "b", "d", "b", "A"),
    ("start", "b", "d", "b"),
    ("start", "b"),
)


def get_graph():
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
        debug(f"{node=}  {path=}  {seen_double=}  {bool(path)=}")

        proceed = False
        if node == "end":
            if settings.settings.debug:
                if (not path) or path[-1] != node:
                    path.append(node)
                self.paths.append(path)
            self.total_paths += 1
            proceed = False
        elif node == "start":
            proceed = False
        elif all(n in string.ascii_lowercase for n in node):
            if node in path:
                if not self.allow_double:
                    proceed = False
                else:
                    if not seen_double:
                        seen_double = True
                        proceed = True
                    else:
                        proceed = False
            else:
                proceed = True
        else:
            proceed = True

        if proceed:
            debug(f"Proceed  {path=}  {node=}")
            if (not path) or path[-1] != node:
                path.append(node)
            for neighbour in self.graph.neighbors(node):
                debug(f"Neighbour  {node=}  {neighbour=}")
                self.process(neighbour, path[:], seen_double)


def process(allow_double):
    graph = get_graph()
    np = NodeProcessor(graph, allow_double=allow_double)
    for node in graph.neighbors("start"):
        np.process(node, [])
    return np.total_paths


def part_1():
    return process(allow_double=False)


def part_2():
    return process(allow_double=True)
