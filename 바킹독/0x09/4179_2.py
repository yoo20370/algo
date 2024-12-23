# 1. 시작점이 두 종류일 때, 먼저 한 시작점에 대하여 BFS를 수행한다.
# 2. 이 문제의 경우에는 불을 먼저 BFS 수행한 후, 불이 번지는 시간을 구해서 graph의 값으로 저장한다.
# 3. 이후 사람이 이동하는 경우에 대하여 BFS를 수행한다. 이때 불이 번지는 시간보다 작은 경우 혹은 번지지 않은 곳에 대하여 BFS를 수행해야 한다. 
import sys
from collections import deque

def miro_escape(miro, row, col) -> int:

    route = ((1, 0), (-1, 0), (0, 1), (0, -1))

    queue = deque()
    fire = deque()
    
    for i in range(row) :
        for j in range(col) :
            if miro[i][j] == 'F':
                fire.append((i, j))
                miro[i][j] = 1
            elif miro[i][j] == '.' :
                miro[i][j] = 0

    while fire :
        curr_row, curr_col = fire.popleft()
        for d_row, d_col in route :
            n_row = curr_row + d_row 
            n_col = curr_col + d_col

            if n_row >= 0 and n_row < row and n_col >= 0 and n_col < col and miro[n_row][n_col] == 0 :
                miro[n_row][n_col] = miro[curr_row][curr_col] + 1
                fire.append((n_row, n_col))

    for i in range(row) :
        for j in range(col) :
            if miro[i][j] == 'J' :
                queue.append((i, j))
                miro[i][j] = 1
                if (i == 0 or i == row - 1 and j < col) or (j == 0 or j == col - 1 and i < row) :
                    return miro[i][j]
    
    while queue :
        curr_row, curr_col = queue.popleft()
        for d_row, d_col in route :
            n_row = curr_row + d_row 
            n_col = curr_col + d_col

            if n_row >= 0 and n_row < row and n_col >= 0 and n_col < col and miro[n_row][n_col] != '#' :
                # 방문하지 않은 경우, 불이 번지기 전에 방문 가능한 경우에 BFS 하게 하면 된다.
                if miro[curr_row][curr_col] + 1 < miro[n_row][n_col] or miro[n_row][n_col] == 0:
                    miro[n_row][n_col] = miro[curr_row][curr_col] + 1
                    queue.append((n_row, n_col))
                    if (n_row == 0 or n_row == row - 1 and n_col < col) or (n_col == 0 or n_col == col -1 and n_row < row) :
                        return miro[n_row][n_col]   
                
    return -1
   

row, col = map(int, sys.stdin.readline().split())

miro = list()

for _ in range(row) :
    miro.append(list(sys.stdin.readline().rstrip()))

result = miro_escape(miro, row, col)
if result == -1 :
    print("IMPOSSIBLE")
else :
    print(result)