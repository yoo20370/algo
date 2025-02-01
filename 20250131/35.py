import sys 

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) -> None :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a 
    else :
        parent[a] = b

N, M = map(int, sys.stdin.readline().split())

edges = []
for _ in range(M) :
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort()

parent = [i for i in range(N + 1)]

last = 0
total_cost = 0
for c, a, b in edges :
    if find_parent(parent, a) != find_parent(parent, b) :
        union(parent, a, b)
        total_cost += c 
        last = c 

print(total_cost - last)
