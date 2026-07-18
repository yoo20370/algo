# 경쟁적 감염 

# 시험관의 바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식
# 매초 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
# 증식 과정에서 특정한 칸에 이미 바이러스가 있다면, 다른 버이러스가 이동 못함
# S초가 지난 후에, (X, Y)에 있는 바이러스 종류를 출력하는 프로그램 작성하라 
# 바이러스가 없다면 0을 출력하라 

# 생각을 해보자 
# 퍼지는 건 bfs를 기반으로 하면 됨 
# 어떤 점을 주의해야 할까 ?? 만약 여러 번의 bfs를 통해서 서로 다른 바이러스가 전염 가능한 위치로 동일한 위치를 큐에 삽입했다면 ?? 
# 수가 작은 것부터 진행하고 이미 처리되었는지 확인이 필요할 것 같다. -> 방문 처리하여 이후 동일한 위치에 대한 감염을 제외시키자
# 그리고 queue에 삽입할 때 시간을 추가해서 특정 시간보다 큰 값이 큐에서 나오게 되면 queue에서 탈출하도록 만들자

# 0 
# 1 0 2 
# 0 0 0
# 3 0 0

# 1
# 1 1 2
# 1 0 2
# 3 3 0

# 2
# 1 1 2 
# 1 1 2
# 3 3 2

# (2, 3) -> (1, 2) = 3 

EMPTYSPACE = 0

from collections import deque 
import sys 

def solution() :

    rowLength, colLength = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(rowLength) :
        inputList = list(map(int, sys.stdin.readline().split()))
        graph.append(inputList)

    targetSecond, targetX, targetY = map(int, sys.stdin.readline().split())

    targetRowIndex = targetX - 1
    targetColIndex = targetY - 1

    # 동, 서, 남, 북
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    currentSecond = 0

    # 일단 삽입할 떄, 바이러스 번호 오름차순으로 큐에 삽입되어 있어야 할 듯 
    # 그냥 List에 삽입한 후, 정렬을 하자 

    virusList = []

    for currentRow in range(rowLength) :
        for currentCol in range(colLength) :
            virusNumber = graph[currentRow][currentCol]
            if virusNumber != EMPTYSPACE :
                virusList.append((virusNumber, currentRow, currentCol, currentSecond))

    virusList.sort()

    queue = deque(virusList)
    
    while queue :
        virusNumber, currentRow, currentCol, currentSecond = queue.popleft()

        # queue에 저장되는 currentSecond는 currentSecond 시간에 감염된 위치를 기록하고 큐에 삽입한 것 (다음 시간에 감염을 진행하기 위해서)
        # 그러므로 targetSecond보다 큰 값이 나오면 queue를 중단해야 함 
        if targetSecond <= currentSecond :
            break

        for currentDirection in directions :
            moveRow, moveCol = currentDirection

            nextRow = currentRow + moveRow
            nextCol = currentCol + moveCol

            # 유효한 시험관이고, 그 공간이 비어있다면 
            if nextRow >= 0 and nextRow < rowLength and nextCol >= 0 and nextCol < colLength and graph[nextRow][nextCol] == EMPTYSPACE :
                graph[nextRow][nextCol] = virusNumber
                queue.append((virusNumber, nextRow, nextCol, currentSecond + 1))

    return graph[targetRowIndex][targetColIndex]

result = solution()
print(result)