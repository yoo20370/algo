import sys
from collections import deque

# bfs를 이용해서 인접한 부분을 탐색하는 방향으로 이동한다. 각 이차원 배열 원소에 값을 움직인 거리로 보고 증가시키는 방향으로 구현 

def bfs(graph, row_size, col_size, start_row, start_col) :

    move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append([start_row, start_col])

    while queue : 
        curr_row, curr_col = queue.popleft()
        
        for next_row, next_col in move_list :
            move_row = curr_row + next_row
            move_col = curr_col + next_col

            if move_row >= 0 and move_row < row_size and move_col >= 0 and move_col < col_size and graph[move_row][move_col] == 1 :
                graph[move_row][move_col] = graph[curr_row][curr_col] + 1
                queue.append([move_row, move_col])

row_size, col_size = map(int, sys.stdin.readline().split())

graph = []
for _ in range(row_size) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


bfs(graph, row_size, col_size, 0, 0)

print(graph[row_size-1][col_size-1])