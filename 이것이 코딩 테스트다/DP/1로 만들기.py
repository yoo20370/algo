# import sys 

# sys.setrecursionlimit(100000)

# N = int(sys.stdin.readline().rstrip())

# MX = 10**6 + 1

# dp = [0] * MX 

# def makeOne(n) :
#     if n == 1 :
#         return 0
    
#     if dp[n] != 0 :
#         return dp[n]

#     result = makeOne(n-1) + 1
#     if n % 3 == 0 :
#         result = min(result, makeOne(n//3) + 1)
#     if n % 2 == 0 :
#         result = min(result, makeOne(n//2) + 1)
    

#     dp[n] = result
#     return dp[n]


# print(makeOne(N))

import sys

N = int(sys.stdin.readline().rstrip())

MX = 10**6 + 1

dp = [-1] * MX

dp[1] = 0 
for i in range(2,N+1) :

    result = dp[i-1] + 1 
    if i % 3 == 0 :
        result = min(result, dp[i//3] + 1)
    if i % 2 == 0 :
        result = min(result, dp[i//2] + 1)
    
    dp[i] = result

print(dp[N])