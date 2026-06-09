# 다익스트라 알고리즘 

## 특정 노드에서 다른 노드까지의 최단거리를 구하는 알고리즘 
## 최단 거리인 노드에 순서대로 접근해서 최단거리를 구하게 된다. 

import sys
import heapq

INF = int(1e9)

def solution() :

    nodeCount, edgeCount = map(int, sys.stdin.readline().split())

    startNode = int(sys.stdin.readline().rstrip())

    graph = [[] for _ in range(nodeCount + 1)]

    for _ in range(edgeCount) :
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append((end, cost))

    # 최단 거리 기록 리스트 
    minDistanceList = [INF] * (nodeCount + 1)

    priorityQueue = []

    minDistanceList[startNode] = 0

    # (지금까지의 총 비용, 현재 노드) 형태로 저장 
    heapq.heappush(priorityQueue, (0, startNode))

    # 가장 최단 거리인 힙 노드를 꺼낸다. 
    while priorityQueue :
        currentCost, currentNode = heapq.heappop(priorityQueue)

        # 중복 처리 방지를 위해 이미 최소 거리를 계산 즉, 방문한 노드라면 건너뛴다. 
        # 최단 거리를 기준으로 계산해 나가므로 이론적으로 최단 거리부터 갱신되어 이후 들어온 거리가 더 길게 됨 
        if minDistanceList[currentNode] < currentCost :
            continue
        
        # 인접한 노드를 순회하면서 비용을 계산 
        for index in range(graph[currentNode]) :
            destinationNode, edgeCost = graph[currentNode][index] 

            totalCost = currentCost + edgeCost 

            # 현재 경우가 최저 비용인 경우 최소 비용 리스트에 기록하고 최소 힙에 저장 
            if minDistanceList[destinationNode] > totalCost :
                minDistanceList[destinationNode] = totalCost
                heapq.heappush(priorityQueue, (totalCost, destinationNode))
        

solution()