# 퇴사 

# N + 1일째 되는 날 퇴사하기로 함 

# Ti가 3이면 오늘포함해서 3일 동안 상담을 하는 거임 
# 1일에 상담을 시작하면 1, 2, 3일에 상담하는 것이므로 4일부터 일할 수 있음 

# 돈을 가장 많이 벌도록 일하는 방향을 해야 함 

import sys

def solution() :
    days = int(sys.stdin.readline().rstrip())

    dp = [0] * (days + 1)
    for day in range(1, days + 1) :

        requireDays, price = map(int, sys.stdin.readline().split())

        # 기록된 것이 없다면 전날 최대값을 가져온다.
        dp[day] = max(dp[day], dp[day - 1])

        # 전날 + 오늘 일하는 거 -> 오늘의 최대값이 될 수 있음 
        if requireDays == 1 :
            dp[day] = max(dp[day], dp[day - 1] + price)

        else :
            # 전날 + 오늘부터 일하는 거
            nextDay = day + requireDays - 1
            if nextDay <= days:
                dp[nextDay] = max(dp[nextDay], dp[day - 1] + price)
        
    print(dp[days])

solution()