val = 0

with open('input.txt', 'r') as f:
    for line in f:
        num = int(line.strip())
        val += num

print(val)
