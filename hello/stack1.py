# 수평으로 탑이 서 있음
# 각 탑은 왼쪽 방향으로 신호를 발사
# 각 탑의 모든 부분에서 수신 가능 -> 같은 높이도 수신 가능 
# 모든 탑은 오른쪽에서 왼쪽으로 신호를 발사함 

# 결국 가장 왼쪽은 최대 N - 1개의 탑을 검사
# 그 다음은 N - 2번 
# 즉, 시간복잡도 O(N**2)의 시간이 걸림 -> 재시간 안에 처리 불가능 -> 탑의 개수 최대 50만개이기 때문
# 여기서 중요한 건 각 탑에서 순회하는 것을 획기적으로 줄여야 한다는 것 
## 신호를 쐈을 때, 안 맞았다면 작은 것, 작은 것이 쐈는데 안 맞았다면 그건 더 작은 것 
## 신호를 발사했을 때, 맞지 않았다면, 스택에 삽입
## 다음 탑이 신호를 발사했을 때 맞았다면, 스택에서 꺼내서 시도 
## 왜냐하면 첫 탑보다 작은 탑이 신호를 쐈을 때 맞췄다는 것은 처음에 쏜 탑도 맞출 가능성이 있기 때문에 확인해야 함 
### 탑에서 왼쪽으로 신호를 쐈을 때 맞았다 -> 바로 기록, 스택이 비어있지 않다면 스택을 확인 그 탑도 맞는지 확인해야 한다. 
### 맞지 않았다. -> 스택에 기록 
### 스택이 맞는 이유는 ?? -> 바로 옆에서 쏜 탑이 맞지 않은 것을 순서대로 처리해야 하기 떄문 

import sys 

def solution() :

    n = int(sys.stdin.readline().rstrip())

    result = [0] * n

    towers = list(map(int, sys.stdin.readline().split()))

    stack = []

    while towers :
        currentTower = towers.pop()
        currentIndex = len(towers)

        # 남은 타워가 있고, 타워가 신호를 수신할 수 있다면 ??
        if towers and currentTower <= towers[-1]:
            result[currentIndex] = len(towers) # 인덱스가 아니라 몇 번째 탑인지이므로 -1을 할 필요가 없음 

            while stack and stack[-1][0] <= towers[-1] :
                currentTower, currentIndex = stack.pop()
                result[currentIndex] = len(towers)

        else : 
            # 타워가 수신하지 못한다면 ??, 스택에 삽입 
            stack.append([currentTower, currentIndex])

    # 코드 하나하나 작성할 때 이유를 들어서 작성해라 
    for tower in range(len(result)) :
        print(result[tower], end = " ")

solution()


