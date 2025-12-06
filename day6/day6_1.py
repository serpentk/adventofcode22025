import functools
import operator

line = ''
problems = []
while True:
    line = input().strip()
    if ('*' in line) or ('+' in line):
        break
    problems.append([int(x) for x in line.split()])

operations = line.split()

print(sum([functools.reduce(operator.add if op == '+' else operator.mul, [line[i] for line in problems]) for i, op in enumerate(operations)]))
