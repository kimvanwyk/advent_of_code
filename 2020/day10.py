from collections import Counter
import functools

import attr
import networkx

import common
from common import debug
import settings


# def build_graph(adapters):
#     graph = networkx.DiGraph()
#     graph.add_node(0)
#     for idx in range(len(adapters) - 1):
#         n = idx - 1
#         node = adapters[idx]
#         while True:
#             next = adapters[n]
#             distance = next - node
#             if distance <= 3:
#                 # graph.add_node(next)
#                 graph.add_edge(node, next, weight=distance)
#                 n += 1
#                 if n >= len(adapters):
#                     break
#             else:
#                 break
#     return graph

def build_graph(adapters):
    graph = networkx.DiGraph()
    graph.add_node(adapters[-1])
    for idx in range(len(adapters) - 1,0,-1):
        n = idx - 1
        node = adapters[idx]
        while True:
            prev = adapters[n]
            distance = node - prev
            if distance <= 3:
                graph.add_edge(node, prev, weight=(-1 * distance))
                n -= 1
                if n < 0:
                    break
            else:
                break
    return graph

# @functools.lru_cache()
# def count_simple_paths(graph, start, end, path, total=0):
#     path = path + (start,)

#     if start == end:
#         total += 1
#         return total

#     for child in graph.successors(start):
#         if child not in path:
#             total = count_simple_paths(graph, child, end, path, total)
#             # child_paths = all_simple_paths(graph, child, end, path)
#             # paths.extend(child_paths)

#     return total

# @functools.lru_cache()
# def count_simple_paths(graph, start, end, total=0):
#     if start == end:
#         total += 1
#         return total

#     for child in graph.successors(start):
#         total = count_simple_paths(graph, child, end, total)

#     return total

@attr.s
class SimplePathCounter():
    start = attr.ib()
    end = attr.ib()
    graph = attr.ib()
    total = attr.ib(default=0)
    stack = attr.ib(default=attr.Factory(list))

    def process_stack_head(self):
        # head is empty, strip off the stack
        if not self.stack[-1]:
            del self.stack[-1]
        else:
            # contents on the stack, pop out next node to consider
            node = self.stack[-1].pop()
            if node == self.end:
                self.total += 1
                debug((self.total, self.stack))
            else:
                next_nodes = [n for n in self.graph.successors(node)]
                if next_nodes:
                    self.stack.append(next_nodes)
        

    def count_paths(self):
        self.total = 0
        self.stack = [[self.start]]
        while self.stack:
            self.process_stack_head()
        return self.total

def process():
    adapters = [n for n in common.read_integer_file()]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters


def part_1():
    adapters = process()
    debug(adapters)
    counter = Counter()
    for n in range(1, len(adapters)):
        counter[adapters[n] - adapters[n - 1]] += 1
    debug(counter)
    return counter[1] * counter[3]


def part_2():
    adapters = process()
    graph = build_graph(adapters)
    print(graph.edges)
    total = 0
    # for p in networkx.all_simple_paths(graph, adapters[-1], adapters[0]):
    #     total += 1
    # total = count_simple_paths(graph, adapters[0], adapters[-1], 0)
    # spc = SimplePathCounter(adapters[0], 12, graph)
    spc = SimplePathCounter(adapters[-1], adapters[0], graph)
    total = spc.count_paths()
    # debug(total)
    return total
