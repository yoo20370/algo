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

graph = []

parent = [i for i in range(v+1)]

for i in range(e) :
    startNode, endNode, cost = map(int, sys.stdin.readline().split())
    graph.append([cost, startNode, endNode])

graph.sort()

totalCost = 0
for currCost, currStartNode, currEndNode in graph :
    if find_parent(parent, currStartNode) != find_parent(parent, currEndNode) :
        union(parent, currStartNode, currEndNode)
        totalCost += currCost

print(totalCost)

