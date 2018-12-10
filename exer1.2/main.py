val = 0
firstRep = None

rep = set()

while firstRep is None:
    with open('input.txt', 'r') as f:
        for line in f:
            num = int(line.strip())

            if firstRep is None and val in rep:
                firstRep = val
            else:
                rep.add(val)

            val += num

print(val)
print(firstRep)
