import sys

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) :
    a = find_parent(parent, a) 
    b = find_parent(parent, b)

    if a < b :
        parent[b] = parent[a]
    else :
        parent[a] = parent[b]

v, e = map(int, sys.stdin.readline().split())

parent = [i for i in range(v+1)]

edges = list()
for i in range(e) :
    start, end, cost = map(int, sys.stdin.readline().split())
    edges.append([cost, start, end])

# 오름차순 정렬 
edges.sort()

sumCost = 0 
for cost, start, end in edges :
    if parent[start] == parent[end] :
        continue
    else :
        union(parent, start, end)
        sumCost += cost

print(sumCost)
