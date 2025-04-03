import sys

order_count, order_length = map(int, sys.stdin.readline().split())

rice_cakes_length = list(map(int, sys.stdin.readline().split()))

# 절단기의 높이를 이진탐색을 수행한다.
# 만약 절단기의 높이 H에서 떡을 잘랐을 때, 떡 길이의 합이 order_length 길이보다 크다면 max_length에 삽입한 후, 절단기의 길이를 높인다. 즉, pl을 중앙값 + 1로 바꾼다.
# 만약 절단기의 높이 H에서 떡을 잘랐을 때, 떡 길이의 합이 order_length 길이보다 작다면 절단기의 길이를 낮춘다. 즉, pr의 값을 중앙값 -1로 바꾼다. 

result = 0

max_length = max(rice_cakes_length)
min_length = 0

while min_length <= max_length :
    curr_length = (min_length + max_length) // 2

    total_length = 0
    for curr_rice_cake_length in rice_cakes_length :
        if curr_rice_cake_length > curr_length :
            total_length += curr_rice_cake_length - curr_length
    
    if order_length <= total_length :
        min_length = curr_length + 1
        result = curr_length
    else :
        max_length = curr_length - 1

print(result)
