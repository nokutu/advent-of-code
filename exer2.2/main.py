from functional import seq

total2 = 0
total3 = 0

with open('input.txt', 'r') as f:
    lines = seq(f.readlines()).map(lambda s: s.strip()).to_list()

    i = 0
    while i < len(lines):
        j = i + 1
        while j < len(lines):
            differ = 0

            res = ''
            for k in range(len(lines[i])):
                if lines[i][k] != lines[j][k]:
                    differ += 1
                else:
                    res += lines[i][k]

            if differ == 1:
                print(res)

            j += 1
        i += 1
