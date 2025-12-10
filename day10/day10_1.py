import sys

def switch(c):
    return '.' if c == '#' else '#'

def push(start, button):
    return ''.join([switch(c) if i in button else c for i, c in enumerate(start)])

def get_lights(goal, buttons):
    cur_count = 0
    to_check = [([], '.' * len(goal))]
    while cur_count < len(buttons):
        for pressed, x in to_check:
            if x == goal:
                return cur_count
        newchecks = []
        for pressed, x in to_check:
            for i, b in enumerate(buttons):
                if pressed and i <= pressed[-1]:
                    continue
                newchecks.append((pressed + [i], push(x, b)))
        to_check = newchecks
        cur_count += 1
    return cur_count

s = 0

for line in sys.stdin:
    data = line.strip().split()
    goal = data[0][1:-1]
    buttons = [[int(x) for x in b[1:-1].split(',')] for b in data[1:-1]]
    c = get_lights(goal, buttons)
    s += c
print(s)
