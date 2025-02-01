
# ## Top-down 방식
# import sys 

# sys.setrecursionlimit(int(1e5))

# N = int(sys.stdin.readline().rstrip())

# MX = 30001
# dp = [MX] * MX
# dp[1] = 0 

# def make_one(n) -> int :
#     if n == 1 :
#         return 0

#     if dp[n] != MX :
#         return dp[n] 
    
#     # 1을 뺀 경우 
#     dp[n] = min(dp[n], make_one(n-1) + 1)

#     if n % 5 == 0 :
#         dp[n] = min(dp[n], make_one(n // 5) + 1)
    
#     if n % 3 == 0 :
#         dp[n] = min(dp[n], make_one(n // 3) + 1)
    
#     if n % 2 == 0 :
#         dp[n] = min(dp[n], make_one(n // 2) + 1)

#     return dp[n]

# print(make_one(N))
    
## Bottom-up 방식 
import sys 

N = int(sys.stdin.readline().rstrip())

MX = 30001

dp = [MX] * MX 
dp[1] = 0

for curr in range(2, N+1) :

    dp[curr] = min(dp[curr], dp[curr-1] + 1)

    if curr % 5 == 0 :
        dp[curr] = min(dp[curr], dp[curr // 5] + 1)

    if curr % 3 == 0 :
        dp[curr] = min(dp[curr], dp[curr // 3] + 1)

    if curr % 2 == 0 :
        dp[curr] = min(dp[curr], dp[curr // 2] + 1)

print(dp[N])