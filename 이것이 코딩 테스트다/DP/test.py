## 개미전사
# Bottom Up 방식 
# import sys

# N = int(sys.stdin.readline().rstrip())

# storages = list(map(int, sys.stdin.readline().split()))

# MX = 101 
# dp = [-1] * MX 

# dp[0] = storages[0]
# dp[1] = max(storages[0],storages[1])

# for i in range(2,N) :
#     dp[i] = max(dp[i-1], dp[i-2] + storages[i])

# print(dp[N-1])

# Top Down 방식
# import sys

# N = int(sys.stdin.readline().rstrip())

# storages = list(map(int, sys.stdin.readline().split()))

# MX = 101

# dp = [-1] * MX 

# dp[0] = storages[0]
# dp[1] = max(storages[0], storages[1])

# def antWairror(n) :
#     if n < 0 :
#         return 0
    
#     if dp[n] != -1 :
#         return dp[n]
    
#     dp[n] = max(dp[n-1], dp[n-2] + storages[n])
#     return dp[n]

# print(antWairror(N-1))

## 바닥 공사
## Bottom up
# import sys 

# N = int(sys.stdin.readline().rstrip())

# MX = 1001
# dp = [0] * (N+1) 

# dp[1] = 1
# dp[2] = 3

# for i in range(3, N+1) :
#     dp[i] = dp[i-1] + dp[i-2] * 2

# print(dp[N])

## Top Down 
# import sys
# N = int(sys.stdin.readline().rstrip())

# MX = 1001

# dp = [0] * MX 

# dp[1] = 1
# dp[2] = 3
# def func(n) :
#     if dp[n] != 0:
#         return dp[n]
    
#     dp[n] = dp[n-1] + dp[n-2] * 2 
#     return dp[n]

# print(func(N))

# 효율적인 화폐 구성 
## Bottom up
# import sys

# N, M = map(int, sys.stdin.readline().split())

# coins = list()
# for i in range(N) :
#     coins.append(int(sys.stdin.readline().rstrip()))

# MX = 10002
# dp = [MX] * (M+1)

# dp[0] = 0 
# for i in range(1,M+1) :
#     for coin in coins :
#         if i - coin >= 0 :
#             dp[i] = min(dp[i],dp[i-coin] + 1)
    
# if dp[M] == 10002:
#     print(-1)
# else :
#     print(dp[M])

# Top Down 
import sys

N, M = map(int, sys.stdin.readline().split())

coins = list()
for i in range(N) :
    coins.append(int(sys.stdin.readline().rstrip()))
    
MX = 10002
dp = [MX] * (M+1)

dp[0] = 0
def func(n) :
    if n < 0 :
        return MX
    
    if dp[n] != MX :
        return dp[n]
    
    for coin in coins :
        dp[n] = min(dp[n], func(n-coin) + 1)

    return dp[n]
    
result = func(M) 
if result == MX :
    print(-1)
else :
    print(result)