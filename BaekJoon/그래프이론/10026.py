import sys, copy
from collections import deque

def bfs(graph, r, c, N, ch, ch2) -> None:

    # 동, 서, 남, 북
    distance = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque() 
    queue.append([r,c])

    graph[r][c] = 'A'

    while queue :
        curr_r, curr_c = queue.popleft()

        for d_r, d_c in distance :
            n_r = curr_r + d_r
            n_c = curr_c + d_c
        
            if n_r >= 0 and n_c >= 0 and n_r < N and n_c < N and (graph[n_r][n_c] == ch or graph[n_r][n_c] == ch2):
                graph[n_r][n_c] = 'A'
                queue.append([n_r, n_c])


N = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(N)]

for i in range(N) :
    for j in sys.stdin.readline().rstrip() :
        graph[i].append(j)

graph2 = copy.deepcopy(graph)

cnt = 0
for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 'R' :
            bfs(graph,i,j,N,'R','R')
            cnt += 1
        elif graph[i][j] == 'G' :
            bfs(graph,i,j,N,'G','G')
            cnt += 1
        elif graph[i][j] == 'B' :
            bfs(graph,i,j,N,'B','B')
            cnt += 1

cnt2 = 0
for i in range(N) :
    for j in range(N) :
        if graph2[i][j] == 'R' or graph2[i][j] == 'G':
            bfs(graph2,i,j,N,'R','G')
            cnt2 += 1
        elif graph2[i][j] == 'B':
            bfs(graph2,i,j,N,'B','B')
            cnt2 += 1

print(cnt, cnt2)
        

