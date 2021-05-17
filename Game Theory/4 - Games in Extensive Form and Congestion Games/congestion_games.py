# 3 person congestion game on acyclic graphs by EXHAUSIVE enumeration
from collections import Counter

# source, target = 0, 4
# graph = {
#     0: (1, 2, 3),
#     1: (4,),
#     3: (4,),
#     2: (1, 3)}
# weights = {
#     (0, 1): (7, 4, 8),
#     (0, 2): (0, 3, 6),
#     (0, 3): (3, 6, 7),
#     (1, 4): (1, 3, 4),
#     (3, 4): (9, 7, 9),
#     (2, 1): (4, 3, 5),
#     (2, 3): (4, 2, 6)
# }

source, target = 0, 4
graph = {
    0: (1, 2, 3),
    1: (4,),
    3: (2, 4),
    2: (1, 4)}
weights = {
    (0, 1): (5, 5, 7),
    (0, 2): (6, 3, 6),
    (0, 3): (4, 9, 5),
    (1, 4): (5, 6, 5),
    (3, 2): (3, 2, 8),
    (3, 4): (7, 8, 7),
    (2, 1): (1, 8, 6),
    (2, 4): (7, 7, 6)
}

def find(s):
    if s == target:
        return [[target]]
    p = []
    for n in graph[s]:
        for subp in find(n):
            p.append([s] + subp)
    return p

def edges(p):
    e = []
    for i in range(len(p) - 1):
        e.append((p[i], p[i + 1]))
    return e

paths = find(source)


min_cost = float('inf')
min_paths = []
n = len(paths)
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            a, b, c = paths[i], paths[j], paths[k]
            d = Counter()
            d.update(edges(a) + edges(b) + edges(c))
            cost = 0
            for ke, v in d.items():
                cost += weights[ke][v - 1] * (v)
            if cost == min_cost:
                min_paths.append([a, b, c])
            if cost < min_cost:
                min_cost = cost
                min_paths = [[a, b, c]]

print('Min cost = ', min_cost)
print('Min paths = ')
for p in min_paths:
    print(p)
