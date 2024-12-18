# Top-Down
# import sys

# N = int(sys.stdin.readline().rstrip())

# dp = [0] * (N+1)

# if N == 1 :
#     dp[1] = 1
# else :
#     dp[1] = 1
#     dp[2] = 3

# def func(n) -> int :
#     if dp[n] != 0 :
#         return dp[n]
    
#     dp[n] = dp[n-1] + dp[n-2] * 2
#     return dp[n]

# print(func(N))

# Bottom-Up
import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * (N+1)

if N > 1 :
    dp[2] = 3
dp[1] = 1
    
def func(n) -> None :
    for idx in range(3,n+1) :
        dp[idx] = dp[idx-1] + dp[idx-2] * 2
    
func(N)

print(dp[N])