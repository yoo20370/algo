import sys
sys.setrecursionlimit(10**6)
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
 
houseCnt, roadCnt = map(int, sys.stdin.readline().split())

edges = []

parent = [ i for i in range(houseCnt + 1)]

for i in range(roadCnt) :
    A, B, cost = map(int, sys.stdin.readline().split())
    edges.append([cost, A, B])

edges.sort()

totalCost = 0
for cost, start, end in edges :
    if find_parent(parent, start) != find_parent(parent, end) :
        totalCost += cost
        union(parent, start, end)

print(totalCost)

