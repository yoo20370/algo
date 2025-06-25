### 가장 긴 증가하는 부분 수열와 유사한 문제

# 병사가 무작위 나열
# 병사는 특정 전투값을 보유 
# 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치하고자 한다. (전투력 높은 병사가 항상 앞에 있어야 함)

import sys 

def solution() :
    solider_count = int(sys.stdin.readline().rstrip())

    soldier_list = list(map(int, sys.stdin.readline().split()))

    memo = [1] * solider_count

    for i in range(solider_count) :
        for j in range(0, i) :
            if soldier_list[i] < soldier_list[j] :
                memo[i] = max(memo[j] + 1, memo[i])
    
    print(solider_count - max(memo))

solution()




