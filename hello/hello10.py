# N * M 크기의 직사각형 
# 각 칸은 육지 또는 바다 
# 케릭터는 동서남북 중 한 곳을 바라본다.

# 캐릭터는 상하좌우로 움직일 수 있음 
# 바다로 되어 있는 공간에는 갈 수 없음 

## 현재 방향 기준으로 왼쪽 방향 부터 차례대로 갈 곳 정함
## 캐릭터의 왼쪽 방향에 아직 가보지 않은 칸이 있다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진 
## 만약 네 방향 모두 이미 가본 칸이라면 바라보는 방향을 유지한채 한 칸 디로 가고 1단계 돌아간다. 
## 이때, 바다인 칸이라 뒤로 갈 수 없는 경우 움직임을 멈춘다. 

import sys 

def solution( ) :

    row, col = map(int, sys.stdin.readline().split())

    currentRow, currentCol, currentDirection = map(int, sys.stdin.readline().split())

    # 북, 동, 남, 서 
    # 0, 1, 2, 3
    moveFrontDirection = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visitCount = 0

    gameMap = []
    for _ in range(row) :
        gameMap.append(list(map(int, sys.stdin.readline().split())))

    while True : 

        # 현재 위치가 육지인지 확인한다. 
        # 육지라면 방문한다. 
        # 0은 방문하지 않은 육지
        # -1은 방문한 육지 
        # 1은 바다 
        if gameMap[currentRow][currentCol] == 0 :
            gameMap[currentRow][currentCol] = -1
            visitCount += 1 
        
        else :
            # 왼쪽으로 돌면서 갈 수 있는 곳이 있는지 확인 
            returnFirstStepFlag = False
            for i in range(1, 5) :
                # 먼저 방향을 틀고 그 방향에 대해서 앞으로 이동할 수 있는지 체크하자 
                nextDirection = currentDirection - i 
                if nextDirection < 0 :
                    nextDirection += 4 

                # 방향 바꾸고 앞으로 이동할 때 좌표 
                moveRow, moveCol = moveFrontDirection[nextDirection]

                nextRow = currentRow + moveRow
                nextCol = currentCol + moveCol
                if nextRow >= 0 and nextRow < row and nextCol >= 0 and nextCol < col and gameMap[nextRow][nextCol] == 0 :
                    # 이동할 수 있다면, 위치 이동하고 처음으로 이동  
                    currentRow = nextRow
                    currentCol = nextCol
                    currentDirection = nextDirection
                    returnFirstStepFlag = True
                    break;
            
            if returnFirstStepFlag :
                continue

            # for문을 모두 돌았음에도 불구하고, 이동할 수 있는 곳이 없는 경우 
            moveRow, moveCol = moveFrontDirection[currentDirection]

            nextRow = currentRow - moveRow
            nextCol = currentCol - moveCol 

            # 방향 유지한채 뒤로 이동했을 때 바다인 경우 종료해야 함 
            if nextRow >= 0 and nextRow < row and nextCol >= 0 and nextCol < col and gameMap[nextRow][nextCol] == 1 :
                break

            # 방향 유지한채 뒤로 이동했을 때 이동할 수 있다면 (육지라면) 좌표 갱신 
            currentRow = nextRow 
            currentCol = nextCol 

        
    return visitCount


print(solution())