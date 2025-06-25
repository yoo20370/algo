# 오늘부터 N + 1일째 되는 날 퇴사를 하기 위해, 남은 n일 동안 최대한 많은 상담을 하려고 함 
# 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡음 

# 3 -> 오늘, 내일, 모레 상담 불가 
# N + 1일 이후에는 회사에 없기 때문에 넘어가면 상담 불가 

## 퇴사전에 할 수 있는 상담의 최대 이익을 구하여라 

##############################################33

# 어떻게 풀 것인가 ??

# 일단은 모든 날짜를 0으로 초기화한다.
# 만약 1일에 T가 3이라면 4일에 현재 최대값 + P 비용과 4일의 현재 최대값을 비교해서 최대값을 memo에 저장하도록 한다. 
# 만약 오늘 상담 시간이 N일을 넘어간다면 넘어가야된다. 

## 결국, memo에 최대값을 저장하도록 해야함 이때, 특정 날짜의 최대값은 전날들의 스케줄에 따라 결정됨 
## 무엇을 놓치고 있는가 ?? 
# -> 특정 날짜에 구한 금액이 상담 가능한 이후 모든 날짜에 적용 가능하다는 것을 놓친듯 -> 반복문으로 최대값 갱신해봐야겠음 

import sys 

def solution() :
    days = int(sys.stdin.readline().rstrip())

    max_value = 0
    memo = [0] * (days + 2)
    for day in range(1, days + 1) :
        time, cost = map(int, sys.stdin.readline().split())

        # 현재 날짜의 상담을 수행할 경우 다음 상담이 가능한 날짜를 target_day
        target_day = day + time 

        # 오늘까지의 최대값에다가 오늘 상담을 수행했을 때 비용을 타겟 날짜의 비용 중 최대값을 저장한다. 
        if target_day <= (days + 1) :
            for index in range(target_day, days + 2) :
                memo[index] = max(memo[index], memo[day] + cost)
    
    print(max(memo))

solution()
