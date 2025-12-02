import re

s = set()
def count_invalid(start, end):
    for x in range(int(start), int(end) + 1):
        x_str = str(x)
        if re.match(r'^(\d+)\1+$', x_str):
            s.add(x)

for v in input().strip().split(','):
    start, end = v.split('-')
    count_invalid(start, end)
    
print(sum(s))
