import sys
from collections import deque


def bfs(graph, r, c, N) -> int :

    # 동, 서, 남, 북
    distance = [(1,0),(-1,0),(0,1),(0,-1)]

    queue = deque()
    queue.append([r,c])
    graph[r][c] = 0 
    size = 1

    while queue :
         
        curr_r, curr_c = queue.popleft()
        
        for d_r, d_c in distance :
            n_r = curr_r + d_r
            n_c = curr_c + d_c

            if n_r >= 0 and n_c >= 0 and n_r < N and n_c < N and graph[n_r][n_c] == 1 :
                graph[n_r][n_c] = 0
                queue.append([n_r,n_c])        
                size += 1

    return size

N = int(sys.stdin.readline().rstrip())

graph = list()

for _ in range(N) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


cnt_arr = list()
cnt = 0
for r in range(N) :
    for c in range(N) :
        if graph[r][c] == 1 :
            cnt_arr.append(bfs(graph, r, c, N))
            cnt += 1
cnt_arr.sort()

print(cnt)
for i in cnt_arr :
    print(i)