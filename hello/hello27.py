# 최소 신장 트리
import sys 

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y) :

    parentX = find(parent, x)
    parentY = find(parent, y)

    if parentX < parentY :
        parent[parentY] = parentX
    else :
        parent[parentX] = parentY 


def solution() :
    nodeCount, edgeCount = map(int, sys.stdin.readline().split())

    edgeList = []

    for _ in range(edgeCount) :
        start, end, cost = map(int, sys.stdin.readline().split())
        edgeList.append((start, end, cost))

    edgeList.sort(key = lambda x : x[2])

    parent = [i for i in range(nodeCount + 1)]

    totalCost = 0
    for index in range(len(edgeList)) :
        start, end, cost = edgeList[index]

        if find(parent, start) != find(parent,end) :
            union(parent, start, end)
            totalCost += cost

    print(totalCost)

solution()