import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())

s_row, s_col, s_dis = map(int, sys.stdin.readline().split())

graph = []

for _ in range(row) :
    graph.append(list(map(int, sys.stdin.readline().split())))

def robot_vacuum_cleaner(row, col, s_row, s_col, s_dis, graph) -> int :

    # 북, 동, 남, 서
    distance = [0, 1, 2, 3]
    turn_left = [3, 0, 1, 2]
    move_forward = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque()
    queue.append((s_row, s_col, s_dis))
    
    clean_count = 0
    while queue :
        c_row, c_col, c_dis = queue.popleft()

        if graph[c_row][c_col] == 0 :
            graph[c_row][c_col] = -1
            clean_count += 1
        
        dis = c_dis
        for _ in range(4):
            # 회전 
            dis = turn_left[dis] # (현재 방향 + 3) % 4를 수행해서 처리할 수 있음

            # 앞으로 이동 
            n_row, n_col = move_forward[dis]

            d_row = c_row + n_row
            d_col = c_col + n_col

            # 청소가 가능하다면
            if d_row >= 0 and d_col >= 0 and d_row < row and d_col < col and graph[d_row][d_col] == 0 :
                queue.append((d_row, d_col, dis))
                break


        else : 
            # 뒤로 이동 
            n_row, n_col = move_forward[c_dis]
            d_row = c_row - n_row
            d_col = c_col - n_col 

            if graph[d_row][d_col] == 1 :
                break
            
            queue.append((d_row, d_col, c_dis))
                
    return clean_count

print(robot_vacuum_cleaner(row, col, s_row, s_col, s_dis, graph))