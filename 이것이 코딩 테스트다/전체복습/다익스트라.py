import sys, heapq

def dijkstra(graph, start) -> None:
    heap = list()
    distance[start] = 0

    heapq.heappush(heap, [0, start])

    while heap :
        currCost, currNode = heapq.heappop(heap)

        # 이미 해당 노드에 대해서 처리했으므로 최단 거리가 짧아질 수 없음 
        if distance[currNode] < currCost :
            continue 
        for endNode, cost in graph[currNode] :
            calCost = currCost + cost 
            if distance[endNode] > calCost :
                distance[endNode] = calCost 
                heapq.heappush(heap, [calCost, endNode])

INF = int(1e9)

node, edge = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(node+1)]

for _ in range(edge) :
    startNode, endNode, cost = map(int, sys.stdin.readline().split())
    graph[startNode].append([endNode, cost])

distance = [INF] * (node + 1)

dijkstra(graph, start)

for idx in range(1, node+1) :
    print(distance[idx])