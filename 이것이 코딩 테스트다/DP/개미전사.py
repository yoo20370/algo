# import sys

# N = int(sys.stdin.readline().rstrip())

# dp = [-1] * N 

# storage = list(map(int, sys.stdin.readline().split()))

# def findMax(arr, curr) :
#     if len(arr) <= curr :
#         return 0
    
#     if dp[curr] != -1 :
#         return dp[curr]
    
#     dp[curr] = arr[curr] + max(findMax(arr, curr+2), findMax(arr, curr+3))
#     return dp[curr]


# print(max(findMax(storage, 0), findMax(storage, 1)))


import sys

N = int(sys.stdin.readline().rstrip())

storage = list(map(int, sys.stdin.readline().split()))

dp = [-1] * N

dp[0] = storage[0]
dp[1] = max(storage[0], storage[1])

maxVal = max(dp[0], dp[1])
for i in range(2, N) :
    dp[i] = max(dp[i-1], dp[i-2] + storage[i])

print(dp[N-1])