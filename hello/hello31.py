# 도시 분할 계획

import sys

def find(village, house) :
    if village[house] != house :
        village[house] = find(village, village[house])
    return village[house]

def union(village, house1, house2) :
    house1Village = find(village, house1)
    house2Village = find(village, house2)

    if house1Village < house2Village :
        village[house2Village] = house1Village
    else :
        village[house1Village] = house2Village


def solution() :

    houseCount, roadCount = map(int, sys.stdin.readline().split())

    roadList = []
    for _ in range(roadCount) :
        a, b, cost = map(int, sys.stdin.readline().split())

        roadList.append([a, b, cost])

    
    roadList.sort(key = lambda x : x[2])

    village = [i for i in range(houseCount + 1)]

    totalCost = 0
    lastCost = 0
    for index in range(roadCount) :
        a, b, cost = roadList[index]

        # 서로 같은 마을에 있지 않다면 
        if find(village, a) != find(village, b) :
            union(village, a, b)
            totalCost += cost
            lastCost = cost


    print(totalCost - lastCost)

solution()