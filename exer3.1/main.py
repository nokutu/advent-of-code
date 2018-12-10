import numpy as np
from functional import seq


def double_data(idata: np.ndarray, idata_side: int) -> (np.ndarray, int):
    new_data_side = idata_side * 2
    new_data = np.zeros((new_data_side, new_data_side), np.int)
    new_data[0:idata_side, 0:idata_side] = idata
    return new_data, new_data_side


data = np.zeros((1000, 1000), np.int)
data_side = 1000

with open('input.txt', 'r') as f:
    for line in f:

        parts = line.strip().split(' ')

        code = int(parts[0][1:])

        tl = seq(parts[2][0:-1].split(',')).map(int).to_list()
        size = seq(parts[3].split('x')).map(int).to_list()

        for i in range(tl[0], tl[0] + size[0]):
            for j in range(tl[1], tl[1] + size[1]):
                if i > data_side or j > data_side:
                    data, data_side = double_data(data, data_side)

                if data[i, j] == 0:
                    data[i, j] = code
                else:
                    data[i, j] = -1

unique, counts = np.unique(data, return_counts=True)
print(dict(zip(unique, counts))[-1])
