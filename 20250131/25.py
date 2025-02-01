
# import sys

# MX = 10001

# N, M = map(int, sys.stdin.readline().split())

# dp = [MX] * (M+1)
# dp[0] = 0 
# coins = list()
# for _ in range(N) :
#     coins.append(int(sys.stdin.readline().rstrip()))


# def func(n) -> int :
#     if n < 0 :
#         return MX 
    
#     if dp[n] != MX :
#         return dp[n]
    
#     for coin in coins :
#         dp[n] = min(dp[n], func(n-coin) + 1)
    
#     return dp[n]

# result = func(M)

# if result >= MX :
#     print(-1)
# else :
#     print(result)

# Botton up 
import sys

MX = 10001

N, M = map(int, sys.stdin.readline().split())

dp = [MX] * (M+1)
dp[0] = 0 
coins = list()
for _ in range(N) :
    coins.append(int(sys.stdin.readline().rstrip()))

for curr in range(1, M+1) :
    for coin in coins :
        if curr - coin >= 0 :
            dp[curr] = min(dp[curr], dp[curr-coin] + 1)

if dp[M] >= MX :
    print(-1)
else :
    print(dp[M])