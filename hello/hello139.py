# 뱀
# 사과를 먹으면 뱀 길이가 늘어난다.
# 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다.

# N * N 정사각 보드 위에서 진행 
# 몇 몇 칸에 사과가 놓여져 있음 
# 보드 상하좌우 끝에는 벽이 있음 

# 맨 위, 맨 좌측에 위치 
# 뱀의 길이는 1
# 처음에는 오른쪽을 향함 

# 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킴
# 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다. 즉, 몸길이는 변하지 않는다.

# 그럼 언제 충돌로 판단할 것인가 ?? 
# 다음 칸으로 위치시켰을 때, 벽 이거나 뱀의 포지션인 경우에는 충돌로 판단하고 게임을 끝내자

# 0은 빈칸
# 1은 뱀의 몸
# 2는 사과 

# 이거 덱쓰면 되는 문제네 ㅋㅋㅋㅋ 

import sys
from collections import deque

LEFT = 'L'
RIGHT = 'D'

def solution() :

    lineSize = int(sys.stdin.readline().rstrip())

    appleCount = int(sys.stdin.readline().rstrip())

    applePosition = set()

    for _ in range(appleCount) :
        row, col = map(int, sys.stdin.readline().split())
        row = row - 1
        col = col - 1
        applePosition.add((row, col))
        

    directionRotationCount = int(sys.stdin.readline().rstrip())

    directionRotationQueue = []
    for _ in range(directionRotationCount) :
        time, direction = sys.stdin.readline().split()
        
        time = int(time)

        directionRotationQueue.append((time, direction))

    directionRotationQueue = sorted(directionRotationQueue)

    directionRotationQueue = deque(directionRotationQueue)

    snakeBodyPosition = deque()
    snakeBodyPosition.append((0,0))

    # 북, 동, 남, 서 
    # 0, 1, 2, 3
    directionMoveList = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    currentDirection = 1
    currentTime = 1

    while True :
        
        if not snakeBodyPosition :
            # 길이가 같거나 길어지기만 하지 줄어들지는 않기 때문 
            print("오류입니다만 ?")

        currentHeadRow, currentHeadCol = snakeBodyPosition[0]

        moveRow, moveCol = directionMoveList[currentDirection]
    
        nextHeadRow = currentHeadRow + moveRow
        nextHeadCol = currentHeadCol + moveCol 

        nextPosition = (nextHeadRow, nextHeadCol)

        # 시간복잡도가 조금 비효율적이긴 하네.. 몸이 길어지면 결국 순회 때문에 길어지니까 
        # 다음 위치가 벽이거나, 뱀의 몸인 경우 
        if nextHeadRow < 0 or nextHeadRow >= lineSize or nextHeadCol < 0 or nextHeadCol >= lineSize or nextPosition in snakeBodyPosition :
            return currentTime

        # 머리 이동
        snakeBodyPosition.appendleft(nextPosition)

        if nextPosition in applePosition :
            applePosition.remove(nextPosition)
        else : 
            snakeBodyPosition.pop()

        # 방향 전환 
        if directionRotationQueue :
            targetTime = directionRotationQueue[0][0]

            if targetTime == currentTime :
                targetTime, command = directionRotationQueue.popleft()

                if command == LEFT :
                    currentDirection = (currentDirection - 1 + 4) % 4 

                else :
                    currentDirection = (currentDirection + 1 + 4) % 4
                    
        currentTime += 1

result = solution()
print(result)