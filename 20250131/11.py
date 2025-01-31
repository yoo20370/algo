import sys 
from collections import deque

def bfs(r, c, row, col, miro) -> None :

    distance = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque()
    queue.append((r,c))

    while queue :
        c_r, c_c = queue.popleft()

        for d_r, d_c in distance :
            n_r = d_r + c_r
            n_c = d_c + c_c
            if n_r >= 0 and n_c >= 0 and n_r < row and n_c < col and miro[n_r][n_c] == 1 :
                miro[n_r][n_c] = miro[c_r][c_c] + 1
                queue.append((n_r, n_c))


row, col = map(int, sys.stdin.readline().split())

miro = list()

for _ in range(row) :
    miro.append(list(map(int, sys.stdin.readline().rstrip())))

bfs(0, 0, row, col, miro)
print(miro[row-1][col-1])





