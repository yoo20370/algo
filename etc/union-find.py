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

for _ in range(e) :
    startNode, endNode = map(int, sys.stdin.readline().split())
    union(parent, startNode, endNode)

for i in range(1, v+1) :
    print(parent[i], end=" ")