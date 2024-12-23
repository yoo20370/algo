import sys
from collections import deque
def bfs(graph, row, col) -> int :

    route = ((1, 0), (-1, 0), (0, 1), (0, -1))

    queue = deque()
    cnt = 0
    temp = 0

    days = 0
    for i in range(row) :
        for j in range(col) :   
            if graph[i][j] == 1 :
                queue.append((i,j))
                temp += 1
            elif graph[i][j] == -1 :
                temp += 1

    while queue :
        curr_row, curr_col = queue.popleft()
        
        for d_row, d_col in route :
            n_row = curr_row + d_row 
            n_col = curr_col + d_col 

            if n_row >= 0 and n_row < row and n_col >= 0 and n_col < col and graph[n_row][n_col] == 0 :
                graph[n_row][n_col] = graph[curr_row][curr_col] + 1
                queue.append((n_row, n_col))
                days = max(days, graph[n_row][n_col])
                cnt += 1
                
    # 모든 토마토가 익어 있는 경우 
    if temp == row * col :
        return 0
    # 정상적으로 계산된 경우
    elif cnt + temp == row * col :
        return days - 1
    # 모두 익지 않은 경우 
    else :
        return -1

col, row = map(int, sys.stdin.readline().split())

graph = list()

for _ in range(row) :
    graph.append(list(map(int, sys.stdin.readline().split())))

print(bfs(graph, row, col))