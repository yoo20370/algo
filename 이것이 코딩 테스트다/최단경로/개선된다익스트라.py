# 개선된 다익스트라 알고리즘 
# O(ElgV), V는 노드의 개수, E는 간선의 개수 
import sys, heapq

INF = int(1e9)
# v는 노드, e는 간선 
v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().rstrip())

visited = [False] * (v+1)
minDis = [INF] * (v+1)

graph = [ [] for i in range(v+1)]

for i in range(e) :
    node, end, val = map(int, sys.stdin.readline().split())
    graph[node].append([end,val])


def dijkstra(start) :
    minHeap = list()
    heapq.heappush(minHeap, (0, start))

    minDis[start] = 0
    while minHeap :
        currDisVal, startNode = heapq.heappop(minHeap) 
        print(currDisVal, startNode)
        # 방문한 노드인 경우 
        if visited[startNode] == True :
            continue

        # 방문 처리 
        visited[startNode] = True
        for endNode, moveCost in graph[startNode] :
            minDis[endNode] = min(minDis[endNode], currDisVal + moveCost)
            heapq.heappush(minHeap, (minDis[endNode], endNode) )

dijkstra(1)

for i in range(1,len(minDis)) :
    if minDis[i] != INF :
        print(minDis[i])
    else :
        print("INF")
        
