# 1 ~ N번 까지의 도시와 M개의 단방향 도로 존재 
# 모든 도로의 거리는 1
# 이때 특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중, 최단 거리가 정확히 K인 도시의 번호를 출력하는 프로그램 작성 

# 최단 거리니까 다익스트라를 사용해야겠군 

import sys, heapq

INF = int(1e9)

def solution() :
    cityCount, loadCount, k, beginCity = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(cityCount + 1)]
    for _ in range(loadCount) :
        begin, end = map(int, sys.stdin.readline().split())
        graph[begin].append(end)

    basicCost = 1
    
    minDistanceList = [INF for _ in range(cityCount + 1)]

    # 시작도시 0 초기화 
    minDistanceList[beginCity] = 0 

    # (현재 도시, 전체 비용)
    priorityQueue = [(beginCity, 0)]

    while priorityQueue :
        currentCity, currentCost = heapq.heappop(priorityQueue)

        if minDistanceList[currentCity] < currentCost :
            continue

        for adjacentCity in graph[currentCity] :
            totalCost = currentCost + basicCost

            # 최단거리가 아니라면 
            if minDistanceList[adjacentCity] > totalCost :
                minDistanceList[adjacentCity] = totalCost
                heapq.heappush(priorityQueue, (adjacentCity, totalCost))
    
    for currentCity in range(1, cityCount + 1) :
        currentCityTotalCost = minDistanceList[currentCity]
        if currentCityTotalCost == k :
            print(currentCity)

solution()