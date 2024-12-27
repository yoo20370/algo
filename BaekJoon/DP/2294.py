import sys

INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())

coins = list()

dp = [INF] * (M+1)

dp[0] = 0
for _ in range(N) :
    coins.append(int(sys.stdin.readline().rstrip()))

for n in range(1, M+1) :
    for coin in coins :
        if n - coin >= 0 :
            dp[n] = min(dp[n], dp[n-coin] + 1)

if dp[M] == INF :
    print(-1)
else :
    print(dp[M])