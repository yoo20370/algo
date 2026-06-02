import sys, heapq

INF = int(1e9)

# 막 풀지말고 생각을 해보자 
# 결국 최단거리 그거 아닌가 ?? 최단 거리인 것부터 방문할거임
# 방문하는데, 최단 거리를 계속 갱신할거임 

def solution() :

    nodeCount, edgeCount = map(int, sys.stdin.readline().split())

    start = int(sys.stdin.readline().rstrip())

    edgeList = [[] for _ in range(nodeCount + 1)]


    for _ in range(edgeCount) :
        startNode, endNode, cost = map(int, sys.stdin.readline().split())

        edgeList[startNode].append((endNode, cost))

    minDistanceCostList = [INF] * (nodeCount + 1) 
    minDistanceCostList[start] = 0 

    priorityQueue = []

    heapq.heappush(priorityQueue, [0, start])

    while priorityQueue :
        currentCost, currentNode = heapq.heappop(priorityQueue)

        # 이미 방문한 경우, 최단거리가 현재보다 작을 수 밖에 없음 
        if minDistanceCostList[currentNode] < currentCost :
            continue

        # 방문하지 않은 경우 최단 거리를 계산해서 최단거리를 갱신하도록 함 
        for index in range(len(edgeList[currentNode])) :
            endNode, endNodeCost = edgeList[currentNode][index]
            totalCost = currentCost + endNodeCost

            # 최단거리 갱신 
            if minDistanceCostList[endNode] > totalCost :
                minDistanceCostList[endNode] = totalCost
                heapq.heappush(priorityQueue, (totalCost, endNode))    

    print(minDistanceCostList)
    

solution()