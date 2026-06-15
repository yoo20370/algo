# 각 칸은 벽 또는 빈칸 
# 청소기는 방향이 있음 (동, 서, 남, 북)
import sys

def solution() :

    rowSize, colSize = map(int, sys.stdin.readline().split())

    currentRow, currentCol, currentDirection = map(int, sys.stdin.readline().split())

    graph = []

    for _ in range(rowSize) :
        inputRow = list(map(int, sys.stdin.readline().split()))
        graph.append(inputRow)

    # 북, 동, 남, 서 
    directions = [0, 1, 2, 3]

    # 방향 회전 
    turnLeft = [3, 0, 1, 2]

    # 북, 동, 남, 서
    moveForward = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    cleanBlockCount = 0

    while True : 
        # 청소되지 않은 경우 
        if graph[currentRow][currentCol] == 0 :
            # 청소한 칸을 2로 정의한다. 
            graph[currentRow][currentCol] = 2
            cleanBlockCount += 1
        
        for _ in range(4) :
            currentDirection = turnLeft[currentDirection]

            moveRow, moveCol = moveForward[currentDirection]

            nextRow = currentRow + moveRow
            nextCol = currentCol + moveCol

            # 청소 여부 확인할 칸이 유효하고, 청소하지 않은 경우라면 
            if nextRow >= 0 and nextRow < rowSize and nextCol >= 0 and nextCol < colSize and graph[nextRow][nextCol] == 0 :
                currentRow = nextRow
                currentCol = nextCol
                break

        else :
            # 한 바퀴를 돌았는데, 청소할 구역이 없는 경우 
            moveRow, moveCol = moveForward[currentDirection]

            nextRow = currentRow - moveRow
            nextCol = currentCol - moveCol

            # 벽이라면 종료해야 함 
            if nextRow >= 0 and nextRow < rowSize and nextCol >= 0 and nextCol < colSize and graph[nextRow][nextCol] == 1 :
                return cleanBlockCount

            else :
                # 벽이 아니라면 방향을 유지한채 뒤로 이동하면 됨 
                currentRow = nextRow 
                currentCol = nextCol 
            
result = solution()
print(result)