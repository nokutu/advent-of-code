import math

chain = ''
with open('input.txt', 'r') as f:
    for line in f:
        chain = line.strip()

i = 0
while i < len(chain) - 1:
    if math.fabs(ord(chain[i]) - ord(chain[i + 1])) == 32:
        chain = chain[:i] + chain[i + 2:]
        i = max(i - 2, -1)
    i += 1

print('Solution:', len(chain))
