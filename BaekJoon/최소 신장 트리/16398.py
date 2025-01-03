import sys

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y) -> None :
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y :
        parent[y] = parent[x]
    else :
        parent[x] = parent[y]

N = int(sys.stdin.readline().rstrip())

edges = list()

for i in range(N) :
    j = 0
    for cost in list(map(int, sys.stdin.readline().split())) :
        if j != 0 :
            edges.append([cost, i, j])
        j += 1

edges.sort()

parent = [i for i in range(N+1)]

total_cost = 0
for cost, start, end in edges :
    if find_parent(parent, start) != find_parent(parent, end) :
        union(parent, start, end)
        total_cost += cost

print(total_cost)
