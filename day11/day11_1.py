import sys
from functools import cache

connections = dict()

@cache
def ways_out(current):
    if current == 'out':
        return 1
    return sum([ways_out(x) for x in connections[current]])


for line in sys.stdin:
    dev, connected = line.strip().split(': ')
    connections[dev] = connected.split()

print(ways_out('you'))
