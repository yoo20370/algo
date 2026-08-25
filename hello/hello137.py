# 화성 탐사 
# 각 칸을 지나기 위한 비용 에너지 소모량 존재
# 0,0 에서 가장 오른쪽인 N-1, N-1 위치로 이동하는 최소 비용을 출력하는 프로그램 작성해라 

# 생각을 해봦 
# BFS와 다익스트라, 플로이드 워셜이 떠오름
# BFS는 적절하지 않은 이유는 비용이 정해진 게 아니고 이동마다 다름 그렇다는 건 전역탐색을 해야함 
# 플로이드 워셜은 안 되는 이유가 입력값은 작은데 n * n 개의 도시에 대해서 구해야 함 그러면 말도 안 됨 
# 다익스트라로 풀어야 하는 이유는 특정 위치에서 특정 위치로 이동하는 경우를 구해야 하기 때문에 bfs, 플로이드 워셜 처럼 모두 계산할 필요가 없음 

import sys, heapq

INF = int(1e9)

def solution() :

    playCount = int(sys.stdin.readline().rstrip())

    for _ in range(playCount) :

        result = getEndPointMinDistance()
        print(result)

def getEndPointMinDistance() :

    n = int(sys.stdin.readline().rstrip())

    graph = []

    for _ in range(n) :
        graph.append(list(map(int, sys.stdin.readline().split())))


    startX = startY = 0
    endX = endY = n - 1
    
    minDistance = [[INF] * n for _ in range(n)]

    minDistance[startX][startY] = graph[startX][startY]

    # 동, 서, 남, 북
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    priorityQueue = []

    # 좌표와 비용을 추가 
    heapq.heappush(priorityQueue, (graph[startX][startY], (startX, startY)))

    while priorityQueue :
        currentCost, locations = heapq.heappop(priorityQueue)
        currentX, currentY = locations

        if minDistance[currentX][currentY] < currentCost :
            continue

        for direction in directions :
            moveX, moveY = direction
            nextX = currentX + moveX 
            nextY = currentY + moveY 

            # 이동 가능한 위치를 확인한다.
            if nextX >= 0 and nextX <= endX and nextY >= 0 and nextY <= endY :
            
                moveCost = graph[nextX][nextY]
                totalCost = currentCost + moveCost
                if minDistance[nextX][nextY] > totalCost :
                    minDistance[nextX][nextY] = totalCost
                    heapq.heappush(priorityQueue, (totalCost, (nextX, nextY)))
                    
    return minDistance[endX][endY]

solution()