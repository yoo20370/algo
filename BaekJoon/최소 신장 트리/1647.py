import sys

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) -> None :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = parent[a]
    elif b < a :
        parent[a] = parent[b]

N, M = map(int, sys.stdin.readline().split())

graph = []

for _ in range(M) :
    start, end, cost = map(int, sys.stdin.readline().split())
    graph.append([cost, start, end])

graph.sort()

parent = [i for i in range(N+1)]

total_cost = 0
last = 0
for cost, start, end in graph :
    if find_parent(parent, start) != find_parent(parent, end) :
        union(parent, start, end)
        total_cost += cost
        last = cost

print(total_cost - last)
