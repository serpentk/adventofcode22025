import sys
import functools
import operator

from scipy.cluster.hierarchy import DisjointSet

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
for d, p1, p2 in distances:
    circuits.merge(p1, p2)
    if len(circuits.subsets()) == 1:
        print(points[p1][0] * points[p2][0])
        break

    
