import sys

# 결국 1 2 3 4 창고가 있을 때, 1, 3번 이냐, 아니면 2, 4이냐 베스트가 될 것이다. 
# 마지막 인덱스 입장에서 마지막 인덱스 값 + 마지막 인덱스 - 2(이때 까지의 최대값)과 마지막 인덱스 -1 (이때까지의 최대값) 중 더 큰 값을 고르는게 핵심
# 즉, memo 테이블에는 각 인덱스까지의 최대값을 저장한다. 구할 수 있는 최대값이 아니라 해당 길이까지의 최대값을 고르는 것 
# memo[0]은 store_list[0]이지만 memo[1]은 0과 1 중에 최대값이 저장되어야 함 

store_count = int(sys.stdin.readline().rstrip())

store_list = list(map(int, sys.stdin.readline().split()))

memo = [0] * (store_count)

memo[0] = store_list[0]
memo[1] = max(store_list[1], memo[0])

for i in range(2, store_count) :
    memo[i] = max((store_list[i] + memo[i-2]), memo[i-1])

print(memo[store_count-1])
