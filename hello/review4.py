# 프림 알고리즘 

# MST를 구하는 방식 
import sys, heapq

def prime() :
    pass

def solution() :
    nodeCount, edgeCount = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(nodeCount + 1)]
    for _ in range(edgeCount) :
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    priorityQueue = []

    heapq.heappush(priorityQueue, (0, 1))

    visited = set()

    totalCost = 0 

    # 가장 거리가 짧은 노드를 꺼내라 
    while priorityQueue :
        currentCost, currentNode = heapq.heappop(priorityQueue)

        # 이미 방문했다면 (집합에 포함되었다면 )
        if currentNode in visited :
            continue

        visited.add(currentNode)
        totalCost += currentCost

        # 방문한 노드의 인접한 노들르 순회
        for index in range(len(graph[currentNode])) :
            adjacentNode, adjacentCost = graph[currentNode][index]

            # 우선순위 큐에 가용치를 기준으로 정렬되도록 배치
            if adjacentNode not in visited :
                heapq.heappush(priorityQueue, (adjacentCost, adjacentNode))


    return totalCost
solution()