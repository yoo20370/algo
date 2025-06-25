# 맨 위층에서 시작해서, 아래에 있는 수중 하나를 선택하여 아래층으로 내려올 때, 
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성해야 한다.

## 삼각형의 크기는 1이상 500이하
## 삼각형을 이루고 있는 각 수는 모두 정수, 0 ~ 9999

###########################################

# 어떻게 풀거야 ?? 
# 아래로 이동하면서 특정 위치의 최대값을 memo에 저장하고자 한다.
# 이때, 각 레벨의 원소를 순회하면서, 왼쪽 아래, 오른쪽 아래에 대해서 수행할 예정 

import sys 

def solution() :
    size = int(sys.stdin.readline().rstrip())

    graph = [] 
    memo = []
    for _ in range(size) :
        data = list(map(int, sys.stdin.readline().split()))
        graph.append(data)
        memo.append([0] * len(data))

    # 초기값 셋팅 
    memo[0] = graph[0]
    
    for row in range(size - 1) :
        for col in range(len(graph[row])) :
            # 현재 레벨은 다음 레빌의 col, col + 1에 대해서 계산해야 함 
            memo[row+1][col] = max(memo[row+1][col], memo[row][col] + graph[row+1][col])
            memo[row+1][col+1] = max(memo[row+1][col+1], memo[row][col] + graph[row+1][col+1])
    
    print(max(memo[size-1]))

solution()

