# Top-Down
# import sys

# length = int(sys.stdin.readline().rstrip())
# stores = list(map(int, sys.stdin.readline().split()))

# dp = [0] * length
# dp[0] = stores[0]
# dp[1] = max(stores[0], stores[1])

# def antWairror(n) -> int:
#     if n == 0 :
#         return dp[0]
    
#     if dp[n] != 0 :
#         return dp[n]
    
#     dp[n] = max(dp[n-1], dp[n-2] + stores[n])
#     return dp[n]

# print(antWairror(length - 1))

# Bottom-Up 
import sys

length = int(sys.stdin.readline().rstrip())
stores = list(map(int, sys.stdin.readline().split()))

dp = [0] * length

dp[0] = stores[0]
dp[1] = max(stores[0], stores[1])

for idx in range(2, length) :
    dp[idx] = max(dp[idx-1], dp[idx-2] + stores[idx])

print(dp[length-1])