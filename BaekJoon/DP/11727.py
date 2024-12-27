import sys

MX = 1001

N = int(sys.stdin.readline().rstrip())

dp = [0] * MX

dp[1] = 1
dp[2] = 3

for n in range(3, MX) :
    dp[n] = dp[n-1] + dp[n-2] * 2

print(dp[N] % 10007)