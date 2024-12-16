import sys, heapq

INF = int(1e9)

# V는 노드, E는 간선 
V, E = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline().rstrip())

distance = [INF] * (V+1)

graph = [[] for _ in range(V+1)]

for _ in range(E) :
    startNode, endNode, cost = map(int, sys.stdin.readline().split())
    graph[startNode].append([endNode, cost])

def dijkstra(start) :

    heap = list()
    distance[start] = 0
    # 우선순위 큐에서 cost가 낮은 것부터 꺼내야 하므로 cost를 기준으로 정렬되도록 cost 먼저 삽입
    # cost가 낮은 것 부터 처리해야 최단 경로가 보장된 상태가 됨
    heapq.heappush(heap, [0, start])

    while heap :
        startNodeCost, startNode = heapq.heappop(heap)

        if distance[startNode] < startNodeCost :
            continue

        for endNode, cost in graph[startNode] :
            totalCost = startNodeCost + cost 

            if distance[endNode] > totalCost :
                distance[endNode] = totalCost 
                heapq.heappush(heap, [totalCost, endNode])

dijkstra(start)

for i in range(1, V+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])
