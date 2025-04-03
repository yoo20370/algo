import sys

data = sys.stdin.readline().rstrip()

# 이동할 수 있는 모든 경우의 수를 배열 형태로 표현한다. 
# 현재 위치에서 모든 경우의 수를 순회하며 가능한 개수를 파악한다.

def move_garden(data) :
    count = 0 

    steps = [(-2,1),(-2,-1), (2,1), (2,-1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

    curr_row = int(ord(data[0]) - ord("a") + 1)
    curr_col = int(data[1])
    
    for row, col in steps:
        now_row = curr_row + row
        now_col = curr_col + col

        if now_row >= 1 and now_row <= 8 and now_col >= 1 and now_col <= 8 :
            count += 1

    
    return count

print(move_garden(data))