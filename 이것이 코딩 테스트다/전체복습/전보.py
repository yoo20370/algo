import sys, heapq

def dijkstra(start, graph, distance) -> int :
    heap = list()
    distance[start] = 0 

    heapq.heappush(heap, [0, start])
    
    # 시작점은 넣지 않으므로 -1로 시작 
    cnt = -1
    maxTime = 0 
    while heap :
        currCost, currCity = heapq.heappop(heap)
        if distance[currCity] < currCost :
            continue

        if maxTime < currCost :
                maxTime = currCost
                
        # 각 도시에는 한 번씩만 접근 가능하므로 접근 가능했을 때 cnt 값을 1 증가시킨다. 
        cnt += 1
        for endCity, cost in graph[currCity] :
            cal_cost = currCost + cost 
            if cal_cost < distance[endCity] :
                distance[endCity] = cal_cost
                heapq.heappush(heap, [cal_cost, endCity])
                

    return cnt, maxTime

INF = int(1e9)

N, M, C = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

distance = [INF] * (N+1)

for _ in range(M) :
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])


cnt, time = dijkstra(C, graph, distance)
print(cnt, time)