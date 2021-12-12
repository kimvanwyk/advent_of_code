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
        if ["start", "A", "b", "A", "c", "A"] == path[:6]:
            print(path)
        for neighbour in self.graph.neighbors(node):
            # debug(f"{node=}  {neighbour=}")
            if neighbour == "end":
                # debug(f"Good path: {path}")
                if settings.settings.debug:
                    if (not path) or path[-1] != node:
                        path.append(node)
                    self.paths.append(path)
                self.total_paths += 1
                continue
            elif neighbour == "start":
                continue
            elif all(n in string.ascii_lowercase for n in neighbour):
                # if ["start", "A", "b", "A", "c", "A"] == path[:6]:
                #     print(f"Small cave: {node=}, {neighbour=}, {path + [node]=}")
                if neighbour in path:
                    # if ["start", "A", "b", "A", "c", "A"] == path[:6]:
                    #     print(f"Double: {node=}, {neighbour=}, {path + [node]=}")
                    if not self.allow_double:
                        continue
                    else:
                        if not seen_double:
                            seen_double = True
                            proceed = True
                        else:
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
    # debug(np.paths)

    # if settings.settings.debug:
    #     unmatched = list(
    #         set(P2_T1_EXPECTED).difference(set((tuple(p) for p in np.paths)))
    #     )
    #     unmatched.sort()
    #     for path in unmatched:
    #         debug(path)
    return np.total_paths
