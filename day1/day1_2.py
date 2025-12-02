import sys

c = 0
pos = 50
for line in sys.stdin:
    direction, value = line[0], int(line[1:])
    delta = value * (1 if direction == 'R' else -1)
    if delta > 0:
        c += (pos + delta) // 100
    elif pos == 0:
        c += -delta // 100
    elif pos + delta <= 0:
        c += -(pos + delta) // 100 + 1
    pos = (pos + delta) % 100
    
print(c)
    
