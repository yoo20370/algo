import sys
from collections import deque

def miro_escape(miro, row, col) -> int:

    route = ((1, 0), (-1, 0), (0, 1), (0, -1))

    queue = deque()

    for i in range(row) :
        for j in range(col) :
            if miro[i][j] == 'J' :
                queue.append((i, j, "route"))
                miro[i][j] = 1
                if (i == 0 or i == row - 1 and j < col) or (j == 0 or j == col - 1 and i < row) :
                        return miro[i][j]

    for i in range(row) :
        for j in range(col) :
            if miro[i][j] == 'F' :
                queue.append((i, j, "fire"))

    while queue :

        curr_row, curr_col, check = queue.popleft()
        # 꺼낸 위치가 불타지 않았다면 
        if check == "route" :
            # 사람의 경로라면 
            if miro[curr_row][curr_col] == 'F' :
                continue 
            for d_row, d_col in route :
                n_row = curr_row + d_row 
                n_col = curr_col + d_col 

                if n_row >= 0 and n_row < row and n_col >= 0 and n_col < col and miro[n_row][n_col] == '.' :
                    miro[n_row][n_col] = miro[curr_row][curr_col] + 1
                    queue.append((n_row, n_col, "route"))

                    # 이동한 위치가 탈출 가능한 위치인 경우
                    if (n_row == 0 or n_row == row - 1 and n_col < col) or (n_col == 0 or n_col == col -1 and n_row < row) :
                        return miro[n_row][n_col]    
                
        else : 
            # 불을 확장
            for d_row, d_col in route :
                n_row = curr_row + d_row 
                n_col = curr_col + d_col 

                if n_row >= 0 and n_row < row and n_col >= 0 and n_col < col and (miro[n_row][n_col] != '#' and miro[n_row][n_col] != 'F'  ):
                    miro[n_row][n_col] = 'F'
                    queue.append((n_row, n_col,"fire"))
            
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