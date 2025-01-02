import sys, copy
from collections import deque

def bfs(graph, row, col, n, h) -> None :

    distance = [(1,0), (-1,0), (0, 1), (0, -1)]
    queue = deque()
    queue.append([row,col])
    graph[row][col] = 0

    while queue :
        r, c = queue.popleft()

        for d_r, d_c in distance :
            n_r = r + d_r 
            n_c = c + d_c 

            if n_r >= 0 and n_r < n and n_c >= 0 and n_c < n and graph[n_r][n_c] > h :
                graph[n_r][n_c] = 0
                queue.append([n_r, n_c])


N = int(sys.stdin.readline().rstrip())

graph = list()

max_val = 0
for i in range(N) :
    data = list(map(int, sys.stdin.readline().split()))
    temp = max(data)
    max_val = max(max_val, temp)
    graph.append(data)

max_cnt = 0
for h in range(0, max_val+1) :
    cnt = 0 
    graph2 = copy.deepcopy(graph)

    for r in range(N) :
        for c in range(N) :
            if graph2[r][c] > h :
                bfs(graph2, r, c, N, h)
                cnt += 1

    max_cnt = max(max_cnt, cnt)
    
print(max_cnt)