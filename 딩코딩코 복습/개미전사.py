import sys 

store_count = int(sys.stdin.readline().rstrip())

store_list = list(map(int, sys.stdin.readline().split()))

dp = [0] * store_count

dp[0] = store_list[0]
dp[1] = max(store_list[0], store_list[1])

# Top Down 
# def ant_warrior(index) -> int :
#     # 제일 마지막 인덱스에서 시작한다. 
#     # 현재 인덱스 - 1의 최대 값과 현재 인덱스의 값 + 현재 인덱스 - 2의 최대값 중 더 큰 값을 골라서 저장한다. 
#     if index <= 1 :
#         return dp[index]
    
#     if index - 2 >= 0 :
#         dp[index] = max(dp[index-1], store_list[index] + dp[index - 2])
    
#     return dp[index]

# Bottom up
def ant_warrior(store_count, store_list) -> int :

    for curr in range(3, store_count) :
        dp[curr] = max(dp[curr - 1], dp[curr - 2] + store_list[curr])

    return dp[store_count - 1]

last_index = store_count - 1

print(ant_warrior(store_count, store_list))