import sys 

N, M = map(int, sys.stdin.readline().split())

rice_cakes = list(map(int, sys.stdin.readline().split()))


# 가장 긴 떡의 길이 
max_length = max(rice_cakes)

min_length = 0

max_height = 0
while min_length <= max_length :
    length = (min_length + max_length) // 2

    total_length = 0
    total_length = sum(max(0, height - length) for height in rice_cakes)

    if total_length < M :
        max_length = length - 1

    elif total_length >= M :
        min_length = length + 1
        max_height = length
print(max_height)
    
        






