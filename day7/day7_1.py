import sys
beams = {input().index('S')}
splits = 0
for line in sys.stdin:
    splitters = {i for i, c in enumerate(line) if c == '^' and i in beams}
    splits += len(splitters)
    beams -= splitters
    beams.update({i + k for i in splitters for k in (1, -1)})

print(splits)
