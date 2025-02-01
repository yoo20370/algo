# Top-down 방식
# import sys

# N = int(sys.stdin.readline().rstrip())

# ant_store = list(map(int, sys.stdin.readline().split()))

# MX = 101

# dp = [-1] * N

# dp[0] = ant_store[0]
# dp[1] = max(dp[0], ant_store[1])

# def ant_warrior(n) :
#     if n < 1 :
#         return dp[n]
    
#     if dp[n] != -1 :
#         return dp[n]
    
#     dp[n] = max(ant_warrior(n-1), ant_warrior(n-2) + ant_store[n])
#     return dp[n]

# print(ant_warrior(len(ant_store)-1))

# Bottom-up 방식 
import sys 

N = int(sys.stdin.readline().rstrip())

ant_store = list(map(int, sys.stdin.readline().split()))

dp = [-1] * N

dp[0] = ant_store[0]
dp[1] = max(dp[0], ant_store[1])

for i in range(2, N) :
    dp[i] = max(dp[i-1], dp[i-2] + ant_store[i])

print(dp[N-1])