# 괴물이 있는 부분0으로, 괴물이 없는 부분은 1로 표시 
# (1, 1)에서 (N, M)으로 이동해야 함 
# 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수 

from collections import deque
import sys 

def solution() :

    rowSize, colSize = map(int, sys.stdin.readline().split())

    # miro 맵을 바탕으로 경로를 탐색해야 하므로 지도를 저장할 필요가 있음 
    miroMap = []
    for _ in range(rowSize) :
        miroMap.append(list(map(int, sys.stdin.readline().rstrip())))

    # (1, 1) -> (0, 0)
    # (N, M) -> (rowSize - 1, colSize - 1)
    currentRow = currentCol = 0

    # (0, 0)에서 이동하면서 한 번 이동시 값을 1증가 시킨다. 이때, 0이거나 1이 아닌 경우는 계산하지 않는다.
    # 0인 경우는 이동 불가
    # 1이 아닌 경우 이미 최소 값으로 이동했을 가능성이 있음 

    # 동, 서, 남, 북
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(currentRow, currentCol)])

    while queue :
        getRow, getCol = queue.popleft()

        # 방문하지 않았으면, 동 서 남 북 이동이 가능한지 확인한다.
        # 방문 가능하다면 큐에 삽입한다.
        for distance in range(len(direction)) :
            moveRow, moveCol = direction[distance]

            nextRow = getRow + moveRow
            nextCol = getCol + moveCol 

            # 1인 경우만 -> 괴물이 있거나 이미 최단 거리로 이동할 수 있는 경우는 제외 
            if nextRow >= 0 and nextRow < rowSize and nextCol >= 0 and nextCol < colSize and miroMap[nextRow][nextCol] == 1 :
                # 현재 위치에서 이동했을 때의 최소 이동거리 값을 기록 
                miroMap[nextRow][nextCol] = miroMap[getRow][getCol] + 1
                queue.append((nextRow, nextCol)) 

    print(miroMap[rowSize - 1][colSize - 1])



solution()