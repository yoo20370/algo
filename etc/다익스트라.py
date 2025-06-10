import sys, heapq

INF = int(1e9)

v, e = map(int, sys.stdin.readline().split())

distance = [INF] * (v+1) 

graph = [ [] for i in range(v+1) ]

start = int(sys.stdin.readline().rstrip())

for _ in range(e) :
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])

def dijkstra(start) :
    h = []
    distance[start] = 0
    heapq.heappush(h, [0, start]) 

    while h :
        currCost, currNode = heapq.heappop(h)

        # 우선순위 큐는 제일 작은 값을 pop한다. 그러므로 
        if distance[currNode] < currCost :
            continue

        for endNode, edgeCost in graph[currNode] :
            # 현재 위치 비용과 가중치 값을 합한 것 
            cost = currCost + edgeCost

            # 만약 distance 배열의 값보다 계산된 cost가 더 작다면 distance 데이터 갱신 
            if distance[endNode] > cost :
                distance[endNode] = cost 
                heapq.heappush(h, [cost, endNode])

dijkstra(1) 

for i in range(1, v+1) :
    if distance[i] == INF :
        print("INF", end=" ")
    else :
        print(distance[i], end=" ")
    

