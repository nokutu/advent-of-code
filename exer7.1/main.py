import math
from typing import List

import numpy as np
from functional import seq
from numba import njit, prange


class Node:
    name: str
    parents: List["Node"]
    sons: List["Node"]

    def __init__(self, name: str):
        self.name = name
        self.parents = []
        self.sons = []

    def pop(self):
        for son in self.sons:
            son.parents.remove(self)


nodes = dict()
with open('input.txt', 'r') as f:
    for line in f:
        parent = line[5:6]
        son = line[36:37]

        if parent not in nodes:
            nodes[parent] = Node(parent)
        if son not in nodes:
            nodes[son] = Node(son)

        nodes[parent].sons.append(nodes[son])
        nodes[son].parents.append(nodes[parent])

ordered_nodes: List[Node] = seq(nodes.values()).order_by(lambda n: n.name).to_list()
res = ''
while len(ordered_nodes) > 0:
    i = 0

    while i < len(ordered_nodes):
        if len(ordered_nodes[i].parents) == 0:
            res += ordered_nodes[i].name
            ordered_nodes[i].pop()
            ordered_nodes.remove(ordered_nodes[i])
            i = 0
        else:
            i += 1

print(res)