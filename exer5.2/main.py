import math

from functional import seq

chain = ''
with open('input.txt', 'r') as f:
    for line in f:
        chain = line.strip()


def react(reactives: str):
    i = 0
    while i < len(reactives) - 1:
        if math.fabs(ord(reactives[i]) - ord(reactives[i + 1])) == 32:
            reactives = reactives[:i] + reactives[i + 2:]
            i = max(i - 2, -1)
        i += 1
    return reactives


letters = set(chain.lower())

min_length = (seq(letters)
              .map(lambda l: chain.replace(l, '').replace(chr(ord(l) - 32), ''))
              .map(react)
              .map(len)
              .min())

print('Solution:', min_length)
