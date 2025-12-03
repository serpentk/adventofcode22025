import sys

c = 0
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        break
    rest = 11
    number = ''
    while rest > 0:
        digit = max(line[:-rest])
        number = number + digit
        maxind = line.index(digit)
        line = line[maxind + 1:]
        rest -= 1
    number = number + max(line)
    c += int(number)
print(c)
    
