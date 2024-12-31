import sys
from collections import deque


def bfs(graph, row, col, r, c) -> int :
    # 동, 서, 남, 북
    distance = [(1,0),(-1,0),(0,1),(0,-1)]

    queue = deque()
    queue.append([r,c]) 
    graph[r][c] = 1
    size = 1

    while queue :
        curr_r, curr_c = queue.popleft()
        
        for d_r, d_c in distance :
            n_r = curr_r + d_r
            n_c = curr_c + d_c

            if n_r >= 0 and n_c >= 0 and n_r < row and n_c < col and graph[n_r][n_c] == 0 :
                graph[n_r][n_c] = 1
                queue.append([n_r,n_c])        
                size += 1
    
    return size

row, col, K = map(int, sys.stdin.readline().split())

graph = [ [0] * col for _ in range(row) ]

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(b, d) :
        for j in range(a, c) :
            graph[i][j] = 1


size_arr = list()
cnt = 0
for i in range(row) :
    for j in range(col) :
        if graph[i][j] == 0 :
            size_arr.append(bfs(graph, row, col, i, j))
            cnt += 1

size_arr.sort()
print(cnt)
for i in size_arr :
    print(i, end=" ")
