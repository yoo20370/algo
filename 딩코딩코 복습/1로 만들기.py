import sys 

X = int(sys.stdin.readline().rstrip())

MX = 10000001


dp = [MX] * (X + 1)

# 탑 다운 방식 
# def makeOne(num) :
#     # 26에서 시작하여 1까지 가는 모든 경우의 수를 재귀호출한다.
#     # num이 1이면 0을 리턴하게 하고 26까지 이동하면서 카운트를 한 개씩 늘려 나간다. 
#     if num == 1 :
#         return 0

#     # 1을 뺀 경우 
#     dp[num] = makeOne(num - 1) + 1

#     # 2으로 나눈 경우
#     if num % 2 == 0 :
#         dp[num] = min(dp[num], makeOne(num // 2) + 1)

#     # 3으로 나눈 경우
#     if num % 3 == 0 :
#         dp[num] = min(dp[num], makeOne(num // 3) + 1)

#     # 5로 나눈 경우 
#     if num % 5 == 0 :
#         dp[num] = min(dp[num], makeOne(num // 5) + 1)

#     return dp[num]

# 바텀업 방식 
def makeOne(num) :

    dp[1] = 0
    for curr in range(2, num + 1) :
        dp[curr] = dp[curr-1] + 1

        if curr % 2 == 0 :
            dp[curr] = min(dp[curr], dp[curr // 2] + 1)
        if curr % 3 == 0 :
            dp[curr] = min(dp[curr], dp[curr // 3] + 1)
        if curr % 5 == 0 :
            dp[curr] = min(dp[curr], dp[curr // 5] + 1)
    
    return dp[num]

print(makeOne(X))

# 정리를 하자면 26에서 갈 수 있는 경우의 수에 대하여 완전 탐색 진행할 것 
# 결국 1에 도달하면 0을 반환, 스택에서 점차 풀어가면 1씩 반환, 이 때, 가능한 경우의 수 중 최소값을 반환하도록 함 
