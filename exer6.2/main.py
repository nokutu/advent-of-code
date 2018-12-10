import math

import numpy as np
from functional import seq
from numba import njit, prange


@njit(parallel=True)
def run(coords: np.ndarray, width: int, height: int) -> int:
    total_area = 0
    for i in prange(width):
        for j in prange(height):
            distances = 0
            for k in prange(coords.shape[0]):
                distances += math.fabs(i - coords[k, 0]) + math.fabs(j - coords[k, 1])
            if distances < 10000:
                total_area += 1

    return total_area


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

if width < 10000:
    tlx -= (10000 - width) // 2
    brx += (10000 - width) // 2
    width = brx - tlx + 1

if height < 10000:
    tly -= (10000 - height) // 2
    bry += (10000 - height) // 2
    height = bry - tly + 1

coords = np.array(seq(coords).map(lambda c: (c[0] - tlx, c[1] - tly)).to_list(), np.int)

print(run(coords, width, height))
