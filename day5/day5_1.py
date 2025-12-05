import sys
fresh = []

line = input().strip()
while len(line) > 0:
    fresh.append([int(x) for x in line.split('-')])
    line = input()

c = 0
for line in sys.stdin:
    ingredient = int(line.strip())
    if any([x[0] <= ingredient <= x[1] for x in fresh]):
        c += 1
print(c)
