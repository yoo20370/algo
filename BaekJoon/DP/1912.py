# import sys

# N = int(sys.stdin.readline().rstrip())

# arr = list(map(int, sys.stdin.readline().split()))

# dp = [[-1001] * (N+1) for i in range(N+1)]

# maxV = -1001
# def func(start, length) :
#     global maxV
#     if length == 1 :
#         if maxV < arr[start] :
#             maxV = arr[start] 
#         return arr[start] 
    
#     if dp[start][length] != -1001 :
#         return dp[start][length]
    
#     pl = start 
#     pr = start + length - 1
#     p = (pl + pr) // 2

#     left = func(pl, (length +1) // 2)
#     right = func(p+1, (length // 2))

#     if maxV < left + right :
#         maxV = left + right 

#     dp[start][length] = left + right    
#     return dp[start][length]

# for length in range(1, N+1) :
#     for start in range(N - length + 1) :
#         func(start, length)

# print(maxV)

import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)

maxVal = -1001
for i in range(1, N+1) :
    dp[i] = max(dp[i-1] + arr[i-1], arr[i-1])
    maxVal = max(dp[i], maxVal)
    
print(maxVal)

