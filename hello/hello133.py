# 화성 탐사

# 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동 할 때, 최적의 경로를 찾도록 개발해야 함 
# 이건 뭘로 풀어야 할까 ??
# bfs ?, 다익스트라 ?, 플로이드?

# bfs는 안 되는게 앞에서 뽑은 것이 최적이라는 보장이 없음 
# 결국 우선순위 큐를 사용해야 함 -> 그래야 앞의 선택이 보장이 됨 

# 다익스트라를 써야 될 것 같음 

# 입력값을 어떻게 활용할 것인가 ?? 
# 인접한 거리로 이동할 수 있다는 것을 활용하면 될 듯 

# 동서남북으로 이동 가능한지 확인하고 이동 가능하면 그 위치까지의 최단거리와 현재 값을 비교하는 방향으로 해야할 듯 

import sys, heapq


INF = int(1e9)

def getMinDistance(startRow, startCol, endRow, endCol, rowLength, colLength, graph) :

    # 동서남북
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

    minDistanceList = [[INF] * colLength for _ in range(rowLength)]

    startCost = graph[startRow][startCol]

    # 시작 지점 초기화 
    minDistanceList[startRow][startCol] = startCost

    priorityQueue = [(startCost, startRow, startCol)]

    while priorityQueue :
        # 해당 위치에 도착했을 때의 좌표와 비용 
        currentCost, currentRow, currentCol= heapq.heappop(priorityQueue)

        # 최단 거리 리스트의 비용보다 현재 비용이 크다면 구할 필요 없음 
        if minDistanceList[currentRow][currentCol] < currentCost :
            continue

        for moveRow, moveCol in direction :

            nextRow = currentRow + moveRow
            nextCol = currentCol + moveCol

            if nextRow >= 0 and nextRow < rowLength and nextCol >= 0 and nextCol < colLength :
                totalCost = currentCost + graph[nextRow][nextCol] 

                # 만약 이동한 위치에 대한 최단거리 보다 지금 구한 최단거리가 작다면, 가능성이 있으므로 수행한다.
                if minDistanceList[nextRow][nextCol] > totalCost :
                    minDistanceList[nextRow][nextCol] = totalCost
                    heapq.heappush(priorityQueue, (totalCost, nextRow, nextCol))

    print(minDistanceList[endRow][endCol])

def solution() :

    totalStage = int(sys.stdin.readline().rstrip())

    startRow = startCol = 0

    for stage in range(totalStage) :

        rowLength = int(sys.stdin.readline().rstrip())
        colLength = rowLength
        
        graph = []

        for row in range(rowLength) :
            colList = list(map(int, sys.stdin.readline().split()))
            graph.append(colList)

        getMinDistance(startRow, startCol, rowLength -1, colLength - 1, rowLength, colLength, graph)


solution()


    
    
    




