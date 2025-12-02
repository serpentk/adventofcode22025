import sys

c = 0
pos = 50
for line in sys.stdin:
    direction, value = line[0], int(line[1:])
    pos = (pos + value * (1 if direction == 'R' else -1)) % 100
    if pos == 0:
        c += 1
print(c)
    
