from functional import seq

total2 = 0
total3 = 0

with open('input.txt', 'r') as f:
    for line in f:
        word = line.strip()

        a = seq(list(word)).count_by_value()

        if a.filter(lambda x: x[1] == 2).any():
            total2 += 1
        if a.filter(lambda x: x[1] == 3).any():
            total3 += 1

print(total2 * total3)

