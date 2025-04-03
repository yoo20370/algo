import sys 

N = int(sys.stdin.readline().rstrip())

dp = [0] * (N + 1) 

dp[1] = 1
dp[2] = 3

# Top-Down 
# def floor_constructure(n) -> int :
#     if n <= 2 :
#         return dp[n]
    
#     if n - 2 >= 1 :
#         dp[n] = dp[n-1] + dp[n-2] * 2

#     return dp[n]

# Bottom Up
def floor_constructure(n) -> int :
    if n <= 2 :
        return dp[2]

    for curr in range(3, n+1) :
        dp[curr] = dp[curr - 1] + dp[curr - 2] * 2
    
    return dp[curr]


print(floor_constructure(N))

