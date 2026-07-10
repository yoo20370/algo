# N x M 크기의 금광 존재 
# 첫 번째 열 부터 채광 시작
# 어떤 행에서 시작하든 상관 없음 
# 이후 m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 함 
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 구하여라

import sys

def mine() :
    row, col = map(int, sys.stdin.readline().split())
    inputList = list(map(int, sys.stdin.readline().split()))

    dp = [[-1] * col for _ in range(row)]

    graph = [[] for _ in range(row)]
    for currentIndex in range(len(inputList)) :
        currentRow = currentIndex // col 

        graph[currentRow].append(inputList[currentIndex])
    
    for index in range(row) :
        dp[index][0] = graph[index][0]

    targetList = [(-1, 1), (0, 1), (1, 1)]   

    for currentCol in range(col - 1) :
        
        # 오른쪽 위, 오른쪽, 오른쪽 아래 
        for currentRow in range(row) :

            for moveRow, moveCol in targetList :
                nextRow = moveRow + currentRow
                nextCol = moveCol + currentCol

                if nextRow >= 0 and nextRow < row and nextCol >= 0 and nextCol < col :
                    dp[nextRow][nextCol] = max(dp[nextRow][nextCol], dp[currentRow][currentCol] + graph[nextRow][nextCol])

    maxValue = 0
    for currentRow in range(row) :
        maxValue = max(maxValue, dp[currentRow][col - 1])

    print(maxValue)

def solution() :

    count = int(sys.stdin.readline().rstrip())

    for _ in range(count) :
        mine()

solution()