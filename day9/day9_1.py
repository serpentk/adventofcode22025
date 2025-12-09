import sys
tiles = []
max_square = 0
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        break
    x, y = [int(a) for a in line.split(',')]
    for t1, t2 in tiles:
        s = abs((t1 - x + 1) * (t2 - y + 1))
        if s > max_square:
            max_square = s
    tiles.append((x, y))
print(max_square)
