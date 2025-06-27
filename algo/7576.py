# 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있다.
# 보관 하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토들의 영향을 받게 된다. 
# 하나의 토마토의 인접한 왼쪽 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
# 대각선 방향에 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정  
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다. 

# 토마토를 창고에 보관하는 격마 모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지 
# 그 최소 일수를 구하는 프로그램을 작성하여라
# 단 상자의 일부 칸에는 토마토가 들어있지 않을 수 있다. 

## 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가  들어있지 않은 칸 

################################
## 어떻게 풀 것인가 
## BFS를 사용해야겠다.
## 익지 않은 토마토를 큐에 넣고, 주변을 탐색하도록 해야겠다.
## 이 때, 시간도 같이 넣어줘야겠다.
## 그리고 처음에 총 몇 개의 토마토가 익어야하는지, 카운트하고
## 익지 않은 토마토를 방문할 때마다 익은 토마토의 개수를 카운트 해준뒤, 1턴이 끝날 때마다 실행하게 할까 생각 중이다.

import sys
from collections import deque

def solution() :
    col, row = map(int, sys.stdin.readline().split())

    box = []
    for _ in range(row) :
        box.append(list(map(int, sys.stdin.readline().split())))
    
    
    total_area_count = row * col
    unripe_tomato = 0
    ripe_tomato = 0
    empty_count = 0

    ## 큐에는 (row, col, day)를 삽입한다.
    queue = deque()

    for r in range(row) :
        for c in range(col) :
            if box[r][c] == 0 :
                unripe_tomato += 1
            elif box[r][c] == 1 :
                ripe_tomato += 1
                queue.append((r,c,0))
            else :
                empty_count += 1
    
    if total_area_count - ripe_tomato - empty_count == 0 :
        return 0


    distance = [(0,1), (0,-1), (1,0), (-1,0)]

    while queue :
        curr_row, curr_col, curr_day = queue.popleft()

        for move_row, move_col in distance :

            next_row = curr_row + move_row
            next_col = curr_col + move_col

            # 상자 범위이고 익지 않은 토마토라면 
            if next_row >= 0 and next_row < row and next_col >= 0 and next_col < col and box[next_row][next_col] == 0 :
                queue.append((next_row, next_col, curr_day + 1))
                box[next_row][next_col] = 1 
                ripe_tomato += 1

                if total_area_count - empty_count - ripe_tomato == 0 :
                    return curr_day + 1

    return -1 

print(solution())