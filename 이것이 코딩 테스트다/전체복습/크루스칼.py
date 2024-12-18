import sys

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) -> None :
    ap = find_parent(parent, a)
    bp = find_parent(parent, b)

    if ap < bp :
        parent[bp] = parent[ap]
    else :
        parent[ap] = parent[bp]

def check_connection(parent, x, y) -> int :
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    # 이미 연결 됨 
    if x == y :
        return 1
    else :
        return 0
    
def kruskal(parent, edges) -> int :
    edges.sort()

    totalCost = 0
    for cost, start, end in edges :
        if not check_connection(parent, start, end) :
            union(parent, start, end)
            totalCost += cost

    return totalCost

node, edge = map(int, sys.stdin.readline().split())

parent = [i for i in range(node+1)]

edges = list()

for _ in range(edge) :
    startNode, endNode, cost = map(int, sys.stdin.readline().split())
    edges.append([cost, startNode, endNode])

print(kruskal(parent, edges))





    
    