# 어두운 길
# 한 마을은 N개의 집과 M개의 도로고 구성 

# 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 도로의 길이와 동일 

# 일부 가로등을 비활성화 하여, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만 오고 갈 수 있도록 만들고자 한다.
# 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램 

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
    houseCount, roadCount = map(int, sys.stdin.readline().split())

    roadList = []

    beforTotalCost = 0 
    for _ in range(roadCount) :
        start, end, cost = map(int, sys.stdin.readline().split())
        roadList.append((cost, start, end))

        beforTotalCost += cost

    sortedRoadList = sorted(roadList)

    parent = [i for i in range(houseCount)]

    afterTotalCost = 0
    for currentRoad in sortedRoadList :

        cost, start, end = currentRoad

        if find(parent, start) != find(parent, end) :
            afterTotalCost += cost
            union(parent, start, end)

    print(beforTotalCost - afterTotalCost)

solution()