# 전보 
# C에서 문제가 발생했을 때 C에서 최대한 많은 곳으로 전보를 보내야 함 
# 즉, C에서 갈 수 있는 모든 도시의 개수를 구해야 함 
# 그리고 C에서 전달해서 이동할 때 각 도시로의 시간도 더 해야 함 -> 언제 더해야 하는가 ??
# 시간을 어떻게 구해야할지 좀 고민임 
# 결국 최단 거리라는게 동시에 진행되는거니까, 이동 가능한 거리 중에서 제일 긴 거 아님 ?? 
# 왜냐하면

import sys, heapq

INF = int(1e9)

def solution() :
    cityCount, routeCount, startCity = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(cityCount + 1)]

    for _ in range(routeCount) :
        start, end, time = map(int, sys.stdin.readline().split())
        graph[start].append((end, time))

    minimunDistanceList = [INF] * (cityCount + 1) 

    priorityQueue = []

    heapq.heappush(priorityQueue, [0, startCity])
    minimunDistanceList[startCity] = 0

    while priorityQueue :
        currentTime, currentCity = heapq.heappop(priorityQueue) 

        if minimunDistanceList[currentCity] < currentTime :
            continue
        

        for index in range(len(graph[currentCity])) :
            endCity, endTime = graph[currentCity][index]
            totalTime = currentTime + endTime

            # 결국 여기가 방문하는 거잖아 그러니까 여기서 마지막에 방문한 값을 구하면 될 것 같은데 
            if minimunDistanceList[endCity] > totalTime :
                minimunDistanceList[endCity] = totalTime
                heapq.heappush(priorityQueue, [totalTime, endCity])

    receiveCityCount = 0
    maxTime = 0
    for index in range(1, len(minimunDistanceList)) :
        if minimunDistanceList[index] != INF :
            receiveCityCount += 1
            maxTime = max(maxTime, minimunDistanceList[index])

    print(receiveCityCount - 1, maxTime)


solution()