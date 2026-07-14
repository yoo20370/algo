# 정수 삼각형 

# 매 층을 내려올 때 왼쪽,오른쪽에 있는 수를 선택할 수 있음 
# 최대합을 구하시오 

# 이전값의 최대값을 알아야 하는 문제 
# 이전값의 최대값을 다시 처음부터 구할 필요는 없음 
# 결국 DP 문제
# 결국 현재 최대값을 구하기 위해서 현재 위치로 올 수 있는 경우에 현재 값을 더해 최대값이 무엇인지 확인하면 됨

import sys

def solution() :

    floorCount = int(sys.stdin.readline().rstrip())
    graph = []

    for _ in range(floorCount) :
        graph.append(list(map(int, sys.stdin.readline().split())))    

    dp = [[-1] * i for i in range(1, floorCount + 1)]

    dp[0][0] = graph[0][0]

    case = [0, 1]

    # 층을 순회하며 현재 위치에서 다음 위치로 계산할 수 있는지 확인할 생각 
    # 마지막 층은 구할 필요가 없음, 이전 층에서 구해서 저장하면 될 듯 
    for currentFloor in range(floorCount - 1) :
        
        for currentIndex in range(len(graph[currentFloor])) :
            
            nextFloor = currentFloor + 1
            for currentCase in case :
                nextIndex = currentIndex + currentCase
                # 다음 경우의 최대값을 구하려면, 다음 경우의 최대값과 현재 경우의 최대값 + 해당 경우의 값을 더한 값 중 큰 값을 구하면 됨
                dp[nextFloor][nextIndex] = max(dp[nextFloor][nextIndex], dp[currentFloor][currentIndex] + graph[nextFloor][nextIndex])

    return max(dp[floorCount - 1])

result = solution()
print(result)