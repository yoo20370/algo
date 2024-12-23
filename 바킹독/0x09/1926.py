import sys 
from collections import deque


def bfs(draw_paper, row, col, row_len, col_len) -> int :

    queue = deque()
    queue.append((row, col))

    route = [(0,1), (0,-1) , (1,0), (-1,0)]

    draw_paper[row][col] = 0

    size = 0

    while queue :
        curr_row, curr_col = queue.popleft()
        size += 1

        for d_row, d_col in route :
            n_row = curr_row + d_row 
            n_col = curr_col + d_col

            if n_row >= 0 and n_row < row_len and n_col >= 0 and n_col < col_len and draw_paper[n_row][n_col] == 1 :
                draw_paper[n_row][n_col] = 0 
                queue.append((n_row, n_col))
                
    return size
    
row, col = map(int, sys.stdin.readline().split())

draw_paper = list()

for i in range(row) :
    draw_paper.append(list(map(int, sys.stdin.readline().split())))

max_size = 0
draw_cnt = 0
for i in range(row) :
    for j in range(col) :
        if draw_paper[i][j] == 1 :
            size = bfs(draw_paper, i, j, row, col)
            max_size = max(max_size, size)
            draw_cnt += 1

print(draw_cnt)
print(max_size)
