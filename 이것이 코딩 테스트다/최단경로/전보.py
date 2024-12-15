import sys, heapq

INF = int(1e9)

cityCnt, routeCnt, startCity = map(int, sys.stdin.readline().split())


distance = [INF] * (cityCnt+1)
graph = [[] for _ in range(cityCnt+1)]

for _ in range(routeCnt) :
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append([end, time])

def dijkstra(start) :
    heap = list()
    heapq.heappush(heap, (0, start))

    while heap :
        currtime, city = heapq.heappop(heap)
        if distance[city] < currtime : 
            continue
        for endCity, time in graph[city] :
            tempTime = currtime + time 
            if distance[endCity] > tempTime :
                distance[endCity] = tempTime
                heapq.heappush(heap, (tempTime, endCity))

dijkstra(startCity)

times = 0
citys = 0
for idx in range(1, cityCnt + 1) :
    if distance[idx] != INF :
        citys += 1
        times = max(times, distance[idx])
print(citys, times)
