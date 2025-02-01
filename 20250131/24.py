# # Top-down 방식 
# import sys 

# N = int(sys.stdin.readline().rstrip())

# dp = [0] * (N+1)
# dp[1] = 1
# dp[2] = 3

# def bottom_construction(n) -> int :
#     if n <= 2 :
#         return dp[n]
    
#     if dp[n] != 0 :
#         return dp[n]
    
#     dp[n] = bottom_construction(n-1) + bottom_construction(n-2) * 2
#     return dp[n]

# print(bottom_construction(N))

# Bottom-Up
import sys 

N = int(sys.stdin.readline().rstrip())

dp = [0] * (N+1)
dp[1] = 1
dp[2] = 3

for i in range(3, N + 1) :
    dp[i] = dp[i-2] * 2 + dp[i-1] % 796796

print(dp[N])