# TopDown 방식 
# import sys

# N, M = map(int, sys.stdin.readline().split())

# dp = [10002] * (M + 1)

# coins = list()
# for i in range(N) :
#     coins.append(int(sys.stdin.readline().rstrip()))

# def func(n) :
#     # 계산 불가능한 경우 
#     if n < 0 :
#         return 10002
#     if n == 0 :
#         return 0
    
#     if dp[n] != 10002 :
#         return dp[n]
    
#     for i in coins :
#         dp[n] = min(dp[n], func(n-i)+1)    

#     return dp[n]
    
# result = func(M)
# if result == 10002 :
#     print(-1)
# else :
#     print(result)


# Bottom Up 방식
import sys

N, M = map(int, sys.stdin.readline().split())

dp = [10002] * (M+1)

coins = list()

for i in range(N) :
    coins.append(int(sys.stdin.readline().rstrip()))

dp[0] = 0

for num in range(M+1) :
    for coin in coins :
        if num-coin >= 0 :
            dp[num] = min(dp[num], dp[num-coin]+1)

if dp[M] == 10002 :
    print(-1)
else :
    print(dp[M])
