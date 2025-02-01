# 크루스칼 알고리즘 
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

v, e = map(int, sys.stdin.readline().split())

edges = []
for _ in range(e) :
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()

parent = [i for i in range(v+1)]

total_cost = 0
for curr_cost, a, b in edges :

    if find_parent(parent, a) != find_parent(parent, b) :
        total_cost += curr_cost
        union(parent, a, b)

print(total_cost)

