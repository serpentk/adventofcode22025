import sys

timelines = {input().index('S'): 1}
for line in sys.stdin:
    splitters = {i for i, c in enumerate(line) if c == '^' and i in timelines}
    splitted = {i: 0 for i in range(len(line))}
    for s in splitters:
        for k in (-1, 1):
            splitted[s + k] += timelines[s]
    timelines = {k: timelines[k] for k in timelines if k not in splitters}
    for s in splitted:
        if s in timelines:
            timelines[s] += splitted[s]
        else:
            timelines[s] = splitted[s]

print(sum(timelines.values()))
