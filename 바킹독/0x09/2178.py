import sys
from collections import deque

def miro_escape(miro, row_len, col_len) -> None :

    queue = deque()
    queue.append((0,0))

    route = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue :
        curr_row, curr_col = queue.popleft()

        for d_row, d_col in route :
            n_row = curr_row + d_row 
            n_col = curr_col + d_col
        
            if n_row >= 0 and n_row < row_len and n_col >= 0 and n_col < col_len and miro[n_row][n_col] == 1 :
                miro[n_row][n_col] = miro[curr_row][curr_col] + 1
                queue.append((n_row, n_col))


row, col = map(int, sys.stdin.readline().split())

miro = list()

for _ in range(row) :
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

miro_escape(miro, row, col)

print(miro[row-1][col-1])