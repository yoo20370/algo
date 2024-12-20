import sys

def cutting(height , arr) -> int :

    total = 0 
    for item in arr :
        if item >= height:
            total += item - height
    return total 

rice_cake_cnt, total_length = map(int, sys.stdin.readline().split())
rice_cakes = list(map(int, sys.stdin.readline().split()))

max_length = max(rice_cakes)

pl = 0 
pr = max_length

height = 0
while pl <= pr :
    curr_height = (pl + pr) // 2

    # 떡의 전체 길이 - (전달기 높이 * 케이스 개수)
    result = cutting(curr_height, rice_cakes)
    # 잘라진 떡의 길이가 원하는 떡의 길이보다 길다면 전달기 높이를 높여서 절단기 최대 높이를 구해야한다. 
    if result >= total_length :
        pl = curr_height + 1
        if height < curr_height :
            height = curr_height
    # 잘라진 떡의 길이가 원하는 떡의 길이보다 짧다면 절단기 높이를 낮춰 정해진 길이로 잘리도록 범위를 정해야 한다.         
    elif result < total_length :
        pr = curr_height - 1
print(height)
    