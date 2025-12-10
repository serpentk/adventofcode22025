import sys
from z3 import *

s = 0

for line in sys.stdin:
    data = line.strip().split()
    joltage = [int(x) for x in data[-1][1:-1].split(',')]
    buttons = [[int(x) for x in b[1:-1].split(',')] for b in data[1:-1]]
    v = IntVector('v', len(buttons))
    solver = Optimize()
    solver.add([x > -1 for x in v])
    for i, j in enumerate(joltage):
        solver.add(j == sum([v[k] for k in range(len(buttons)) if i in buttons[k]]))
    presses = solver.minimize(sum([x for x in v]))
    assert(solver.check() == sat)
    s += presses.value().as_long()
print(s)
