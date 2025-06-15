# 각 계단에서 가능한 경우의 수를 모두 기록한다. 
# 마지막 계단 전까지는 전에서 온 경우와 전전에서 온 경우를 모두 기록한다.
# 인덱스 0에는 다음 칸으로 이동 가능한 경우 인덱스 1에는 다다음 칸 이동 가능 

import sys 

def up_stair() :
    stair_count = int(sys.stdin.readline().rstrip())

    stair_list = [0] 
    for _ in range(1, stair_count + 1) :
        stair_list.append(int(sys.stdin.readline().rstrip()))

    memo = [[0] * 2 for _ in range(stair_count + 1)]

    memo[1][0] = stair_list[1]
    memo[1][1] = stair_list[1]

    for index in range(2, stair_count + 1) :
        memo[index][1] = memo[index - 1][0] + stair_list[index]
        memo[index][0] = max(memo[index - 2][1], memo[index - 2][0]) + stair_list[index]
    
    print(max(memo[stair_count]))

up_stair()

# 이건 뭐임 ?? ㅋㅋㅋㅋㅋㅋㅋㅋ
# n = int(input())

# stairs = [0] * 301
# for i in range(1, n + 1):
#     stairs[i] = int(input())

# dp = [0] * 301
# dp[1] = stairs[1]
# dp[2] = stairs[1] + stairs[2]
# dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# for i in range(4, n + 1):
#     dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

# print(dp[n])