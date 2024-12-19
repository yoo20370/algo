# Top-Down
# import sys

# MX = 10001

# coin_cnt, total_money = map(int, sys.stdin.readline().split())

# coins = list()

# for i in range(coin_cnt) :
#     coins.append(int(sys.stdin.readline().rstrip()))

# dp = [MX] * (total_money + 1)

# dp[0] = 0
# def func(n, coins) -> int :
#     if n < 0 :
#         return MX
    
#     if n == 0 :
#         return 0
    
#     if dp[n] != MX :
#         return dp[n]
    
#     for coin in coins :
#         dp[n] = min(dp[n], func(n-coin, coins) + 1)
    
#     return dp[n]

# result = func(total_money, coins)
# if result == MX :
#     print(-1)
# else :
#     print(dp[total_money])
    
# Bottom-Up
import sys

MX = 10001

coin_cnt, total_money = map(int, sys.stdin.readline().split())

coins = list()

for i in range(coin_cnt) :
    coins.append(int(sys.stdin.readline().rstrip()))

dp = [MX] * (total_money + 1)

dp[0] = 0
for idx in range(1, total_money+1) :
    for coin in coins :
        if idx - coin >= 0 :
            dp[idx] = min(dp[idx], dp[idx-coin] +1)

if dp[total_money] == MX :
    print(-1)
else :
    print(dp[total_money])
    
