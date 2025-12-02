s = set()
def count_invalid(start, end):
    for x in range(int(start), int(end) + 1):
        x_str = str(x)
        if len(x_str) % 2 != 0:
            continue
        if x_str[:len(x_str)//2] == x_str[len(x_str)//2:]:
            s.add(x)

for v in input().strip().split(','):
    start, end = v.split('-')
    count_invalid(start, end)
    
print(sum(s))
