import sys

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y) -> None :
    xp = find_parent(parent, x)
    yp = find_parent(parent, y)

    if xp < yp :
        parent[yp] = parent[xp]
    else :
        parent[xp] = parent[yp] 

# 연결되어 있다면 1 반환, 그렇지 않다면 0 반환 
def check_connection(parent, x, y) -> int :
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    # 이미 연결 됨 
    if x == y :
        return 1
    else :
        return 0

node, edge = map(int, sys.stdin.readline().split())

parent = [i for i in range(node+1)]

for _ in range(edge) :
    startNode, endNode = map(int, sys.stdin.readline().split())
    union(parent, startNode, endNode)

for idx in range(1, node +1) :
    print(parent[idx], end=" ")