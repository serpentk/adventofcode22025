import functools
import operator

line = ''
problems = []
while True:
    line = input()
    if ('*' in line) or ('+' in line):
        break
    problems.append(line)

operations_line = line

op = None
to_operate = []
res = 0
for i, c in enumerate(operations_line):
    if c == '*':
        op = operator.mul
    elif c == '+':
        op = operator.add
    if all([x[i] == ' ' for x in problems]):
        if op is not None:
            res += functools.reduce(op, to_operate)
        to_operate = []
        continue
    to_operate.append(int(''.join([x[i] for x in problems]).strip()))

if op is not None:
    res += functools.reduce(op, to_operate)
print(res)
