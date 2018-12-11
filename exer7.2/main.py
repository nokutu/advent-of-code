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

    def get_duration(self) -> int:
        return 60 + ord(self.name) - 64


class Worker:
    work_duration: int
    work_start: int
    work_node: Node

    def __init__(self):
        self.work_duration = -1
        self.work_start = -1
        self.work_node = None

    def is_free(self, time: int) -> bool:
        return time >= self.work_start + self.work_duration

    def work(self, time: int, node: Node):
        self.work_start = time
        self.work_duration = node.get_duration()
        self.work_node = node

    def just_finished(self, time: int) -> bool:
        return time == self.work_start + self.work_duration


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

workers = [Worker() for i in range(5)]
time = 0
ordered_nodes: List[Node] = seq(nodes.values()).order_by(lambda n: n.name).to_list()
res = ''
target_len = len(ordered_nodes)
while len(res) < target_len:
    i = 0

    for worker in workers:
        if worker.just_finished(time):
            res += worker.work_node.name
            worker.work_node.pop()

    while i < len(ordered_nodes):
        if len(ordered_nodes[i].parents) == 0:

            if seq(workers).filter(lambda w: w.is_free(time)).any():
                worker = seq(workers).filter(lambda w: w.is_free(time)).first()
                worker.work(time, ordered_nodes[i])
                ordered_nodes.remove(ordered_nodes[i])
                i -= 1

        i += 1

    time += 1

print(res)
print(time - 1)
