import sys
import functools
import operator

from scipy.cluster.hierarchy import DisjointSet

NSTEPS = 1000
N_LARGEST_CIRCUITS = 3

distances = []
points = []

for i, line in enumerate(sys.stdin):
    line = line.strip()
    if len(line) == 0: break
    x, y, z = [int(x) for x in line.split(',')]
    for j, (px, py, pz) in enumerate(points):
        distances.append(((px -x) * (px - x) + (py - y) * (py -y) + (pz - z) * (pz - z), j, i))
    points.append((x, y, z))

distances.sort()
circuits = DisjointSet(range(len(points)))
for d, p1, p2 in distances[:NSTEPS]:
    circuits.merge(p1, p2)

print(functools.reduce(
    operator.mul,
    [len(x) for x in sorted(circuits.subsets(), key=lambda x: len(x), reverse=True)][:N_LARGEST_CIRCUITS]))


    
