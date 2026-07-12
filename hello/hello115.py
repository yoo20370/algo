# 연구소 
# 바이러스의 확산을 막기 위해 연구소에 벽을 세우려고 함 
# 바이러스가 상하 좌우로 인접한 빈칸으로 모두 퍼져나감 
# 새로 세울 수 있는 벽의 개수는 3개, 꼭 3개를 세워야 함 
# 0은 빈칸, 1은 벽, 2는 바이러스 
# 결국 모든 경우를 확인해봐야 하는 거 아닌가 ?? -> 어디에 둬야 최적일지 알 수 없음 
## 바로 떠오른 생각은 백트래킹을 통해서 빈칸에 벽을 세운다. 
## bfs 탐색을 통해서 바이러스를 퍼뜨린다.
## 빈칸의 개수를 확인한다. 

# 현재 문제점 
# 백트래킹이 순열로 동작하고 있음 그러므로 조합으로 수정해야 함 
# startIndex를 추가해서 조합으로 동작하도록 수정 
# 즉, startIndex 이전의 원소는 이미 선택된 것으로 간주하게 함

import sys 
from collections import deque

EMPTY = 0
WALL = 1
VIRUS = 2

INIT = 0

# 동, 서, 남, 북 
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 결국 모든 벽을 설치했을 떄 모든 바이러스에 대해서 bfs를 수행하도록 하는게 좋을 듯 
# 그리고 매번 모든 row 돌지 말고, 바이러스 시작점은 미리 계산해 두는게 좋을 듯 
def installWall(avaliableInstallWallCount, rowLength, colLength, startIndex, wallLocation, emptyLocation, virusLoaction, graph) :

    global direction
    maxCount = INIT
    
    # 벽이 세 개 세워졌을 떄 
    # 종료 조건
    if avaliableInstallWallCount == 0 :
        
        queue = deque(virusLoaction)

        visited = set()

        while queue :
            currentRow, currentCol = queue.popleft()
            
            for moveRow, moveCol in direction :

                nextRow = currentRow + moveRow
                nextCol = currentCol + moveCol 

                # 유효한 범위이고 빈칸인 경우 
                if nextRow >= 0 and nextRow < rowLength and nextCol >= 0 and nextCol < colLength and graph[nextRow][nextCol] == EMPTY :
                    nextLocation = (nextRow, nextCol)
                    # 빈칸이고, 아직 방문되지 않는 곳이라면 
                    if nextLocation not in visited :
                        queue.append(nextLocation)
                        visited.add(nextLocation)
        
        totalCount = rowLength * colLength
        virusCount = len(visited) + len(virusLoaction)
        wallCount = len(wallLocation) + 3
        emptyCount = totalCount - virusCount - wallCount
        
        return emptyCount
    
    # 백트래킹을 통해서 벽을 세워야 함 
    # 문제 축소 
    for index in range(startIndex, len(emptyLocation)) :
        emptyRow, emptyCol = emptyLocation[index]
    
        graph[emptyRow][emptyCol] = WALL
        maxCount = max(maxCount, installWall(avaliableInstallWallCount - 1, rowLength, colLength, index + 1, wallLocation, emptyLocation, virusLoaction, graph))
        graph[emptyRow][emptyCol] = EMPTY

    return maxCount

def solution() :

    rowLength, colLength = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(rowLength) :
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    emptyLocation = []
    virusLocation = []
    wallLocation = []

    # 매번 순회하면 오래 걸리니 원래 위치를 미리 구해둔다.
    for row in range(rowLength) :
        for col in range(colLength) :
            currentLocation = (row, col)
            if graph[row][col] == VIRUS :
                virusLocation.append(currentLocation)
            elif graph[row][col] == EMPTY :
                emptyLocation.append(currentLocation)
            else :
                wallLocation.append(currentLocation)

    return installWall(3, rowLength, colLength, 0, wallLocation, emptyLocation, virusLocation, graph)

    
    

print(solution())
