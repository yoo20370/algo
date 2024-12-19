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

def check_connetion(parent, x, y) -> bool :
    if find_parent(parent, x) == find_parent(parent, y) :
        return True 
    return False

def cityDivPlan(edges, parent) -> int :

    totalCost = 0
    last = 0
    for cost, start, end in edges :
        if not check_connetion(parent, start, end) :
            union(parent, start, end)
            totalCost += cost
            last = cost
    
    return totalCost - last



N, M = map(int, sys.stdin.readline().split())

edges = []

for _ in range(M) :
    start, end, cost = map(int, sys.stdin.readline().split())
    edges.append([cost, start, end])

edges.sort()

parent = [i for i in range(N+1)]

print(cityDivPlan(edges, parent))