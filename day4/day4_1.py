import sys

grid = [line.strip() for line in sys.stdin]

x_len, y_len = len(grid[0]), len(grid)
c = 0
for y in range(y_len):
    for x in range(x_len):
        if grid[y][x] == '.':
            continue
        neibours = [(a, b)
                    for a in (y - 1, y, y + 1)
                    for b in (x - 1, x, x + 1)
                    if -1 < a < y_len and -1 < b < x_len and (a, b) != (y, x) and grid[a][b] == '@']
        if len(neibours) < 4:
            c += 1

print(c)
