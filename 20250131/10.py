import sys
from collections import deque 

# def dfs(r, c, row, col, graph) -> None :
#     # 동, 서, 남, 북 
#     distance = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#     queue = deque()
#     queue.append((r,c))
#     graph[r][c] = 1

#     while queue :
#         c_r, c_c = queue.popleft()

#         for d_r, d_c in distance :
#             n_r = d_r + c_r
#             n_c = d_c + c_c

#             if n_r >= 0 and n_c >= 0 and n_r < row and n_c < col and graph[n_r][n_c] == 0 :
#                 graph[n_r][n_c] = 1
#                 queue.append((n_r, n_c))

def dfs(r, c, row, col, graph) -> None :
    distance = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    graph[r][c] = 1

    for d_r, d_c in distance :
        n_r = d_r + r
        n_c = d_c + c 

        if n_r >= 0 and n_c >= 0 and n_r < row and n_c < col and graph[n_r][n_c] == 0 :
            graph[n_r][n_c] = 1
            dfs(n_r, n_c, row, col, graph)

row, col = map(int, sys.stdin.readline().split())

pan = list()
for i in range(row) :
    pan.append(list(map(int, sys.stdin.readline().rstrip())))

cnt = 0 
for r in range(row) :
    for c in range(col) :
        if pan[r][c] == 0 :
            dfs(r,c,row,col,pan)
            cnt += 1

print(cnt)