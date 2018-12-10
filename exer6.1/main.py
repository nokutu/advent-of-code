import math
import numpy as np
from functional import seq
from numba import njit


@njit()
def grow_loop(source_m: np.ndarray) -> np.ndarray:
    current_m = source_m
    next_m = current_m.copy()

    while True:
        for i in range(source_m.shape[0]):
            for j in range(source_m.shape[1]):
                if current_m[i, j] != -1:
                    grow_pixel(current_m, next_m, i, j)

        if np.where(next_m == -1)[0].size == 0:
            return next_m
        else:
            current_m = next_m.copy()


@njit()
def grow_pixel(current_m: np.ndarray, next_m: np.ndarray, i: int, j: int):
    for x, y in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        if i == 0:
            x = max(x, 0)
        elif i == current_m.shape[0] - 1:
            x = min(x, 0)
        if j == 0:
            y = max(y, 0)
        elif j == current_m.shape[1] - 1:
            y = min(y, 0)

        if current_m[i + x, j + y] == -1:
            if next_m[i + x, j + y] == -1:
                next_m[i + x, j + y] = current_m[i, j]
            elif next_m[i + x, j + y] != current_m[i, j]:
                next_m[i + x, j + y] = -2


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

sol = grow_loop(matrix)

unique, counts = np.unique(sol, return_counts=True)
results = dict(zip(unique, counts))

to_remove = sol.copy()
to_remove[1:-1, 1:-1] = -2

unique, counts = np.unique(to_remove, return_counts=True)

for v in unique:
    del results[v]

biggest = (seq(results).map(lambda k: (k, results[k])).max_by(lambda p: p[1]))

print(biggest)
