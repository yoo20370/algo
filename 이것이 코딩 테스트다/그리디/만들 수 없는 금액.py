# # 백준 2437
# import sys 
# import itertools

# MX = 1000000
# dp = [-1] * MX

# N = int(sys.stdin.readline().rstrip())
# coins = list(map(int, sys.stdin.readline().split()))

# for i in range(1, len(coins)+1) :
#     result = set(itertools.combinations(coins, i))

#     for j in result :
#         idx = sum(j)
#         dp[idx] = 1

# curr_coin = 1
# while True :
#     if dp[curr_coin] == -1 :
#         print(curr_coin)
#         break
#     curr_coin += 1

