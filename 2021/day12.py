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
    def __init__(self, graph):
        self.graph = graph
        self.total_paths = 0

    def process(self, node, path):
        for neighbour in self.graph.neighbors(node):
            # debug(f"{node=}  {neighbour=}")
            if neighbour == "end":
                # debug(f"Good path: {path}")
                self.total_paths += 1
                continue
            elif neighbour == "start":
                continue
            elif (all(n in string.ascii_lowercase for n in neighbour)) and (
                neighbour in path
            ):
                # hit a small cave again
                # debug(f"Bad path (goes to {node}): {path}")
                continue
            else:
                path.append(node)
                self.process(neighbour, path[:])


def part_1():
    graph = process()
    np = NodeProcessor(graph)
    np.process("start", [])
    return np.total_paths


def part_2():
    return process()
