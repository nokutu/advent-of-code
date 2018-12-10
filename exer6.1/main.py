import math
import numpy as np
from functional import seq


def grow_loop(source_m: np.ndarray):
    current_m = source_m
    next_m = np.full(source_m.shape, -1)

    # TODO

    if next_m[next_m == -1].size == 0:
        return next_m


coords = []
with open('input.txt', 'r') as f:
    for line in f:
        coords.append(seq(line.strip().split(',')).map(int).to_list())

tlx = seq(coords).map(lambda c: c[0]).min()
tly = seq(coords).map(lambda c: c[1]).min()
brx = seq(coords).map(lambda c: c[0]).max()
bry = seq(coords).map(lambda c: c[1]).max()

width = brx - tlx + 1
height = bry - tly + 1

matrix = np.full((width, height), -1)

for pos, coord in enumerate(coords):
    matrix[coord[0] - tlx, coord[1] - tly] = pos

grow_loop(matrix)
