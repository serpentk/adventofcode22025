import sys

c = 0
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        break
    first = max(line[:-1])
    maxind = line.index(first)
    second = max(line[maxind + 1:])
    c += int(first + second)
print(c)
    
