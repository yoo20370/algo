import sys

N, M = map(int, sys.stdin.readline().split())

max_value = 0
for _ in range(N) :
    # 값이 들어왔을 때 최소값을 구한 후 최대값을 비교하여 더 크면 저장한다. 
    cards = list(map(int, sys.stdin.readline().split()))
    min_num = min(cards)

    if max_value < min_num :
        max_value = min_num
    
print(max_value)
    

    

