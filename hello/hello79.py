# 게임맵 최단 거리
# dfs 보다 bfs로 풀려고 한다.
# 그 이유는 4방면을 모두 탐색해서 확인하는 과정을 수행하려고 함 
from collections import deque

def solution(maps):
    
    row = len(maps)
    col = len(maps[0])
    
    # 동, 서, 남, 북
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 시작 지점
    currentRow = currentCol = 0
    destinationRow = row - 1
    destinationCol = col - 1
    
    queue = deque()
    queue.append([currentRow, currentCol])
    
    while queue : 
        currentRow, currentCol = queue.popleft()
        
        for moveRow, moveCol in direction :
            nextRow = currentRow + moveRow
            nextCol = currentCol + moveCol
            
            if nextRow >= 0 and nextRow < row and nextCol >= 0 and nextCol < col and maps[nextRow][nextCol] == 1 :
                maps[nextRow][nextCol] = maps[currentRow][currentCol] + 1
                queue.append([nextRow, nextCol])
        
    
    
    result = maps[destinationRow][destinationCol]
    if maps[destinationRow][destinationCol] == 1 :
        result = -1
        
    return result