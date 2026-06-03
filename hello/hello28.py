# 프림 알고리즘 
import sys, heapq

def solution() :
    nodeCount, edgeCount = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(nodeCount + 1)]

    for _ in range(edgeCount) :
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append((end,cost))
        graph[end].append((start,cost))


    result = prime(graph, 1) 
    print(result)


def prime(graph, startNode) :

    priorityQueue = []
    visited = set()

    heapq.heappush(priorityQueue, (0, startNode))

    totalCost = 0

    while priorityQueue :
        cost, node = heapq.heappop(priorityQueue)

        if node in visited : 
            continue

        visited.add(node)
        totalCost += cost

        for index in range(len(graph[node])) :
            currentNode, currentCost = graph[node][index]
            
            if currentNode not in visited :
                heapq.heappush(priorityQueue, (currentCost, currentNode))
    return totalCost

solution()