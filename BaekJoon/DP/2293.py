import sys

n, k = map(int, sys.stdin.readline().split())

coins = list()

dp = [-1] * (k+1)

for _ in range(n) :
    coins.append(int(sys.stdin.readline().rstrip()))

dp[0] = 0 
for i in range(1, k + 1):
    
    for coin in coins :
        if i - coin > -1 and dp[i-coin] != - 1 :
            if dp[i-coin] == 0 :
                dp[i] = dp[i-coin] + 1

print(dp[k])