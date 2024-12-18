# dfs 사용 시 한 번에 연결된 모든 공간을 탐색하고, 더 이상 연결된 노드가 없을 때 되돌아온다. 
# bfs 사용 범위를 점진적으로 확장하지만 큐에 많은 노드가 쌓이게 되면 메모리 사용량이 증가할 수 있다. 
# 반면 DFS는 재귀 호출 스택 또는 명시적인 스택을 사용하므로 메모리 사용량이 탐색 깊이에 비례합니다.

import sys

row, column = map(int, sys.stdin.readline().split())

graph = []

# 동, 서, 남, 북 y, x
check = [(1,0), (-1, 0),(0,1),(0,-1)]


for i in range(row) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(graph, y, x) -> None:

    # 방문 처리 
    graph[y][x] = 1

    for dx, dy in check :
        currX = x + dx 
        currY = y + dy
        # 범위 내인 경우 그리고 방문하지 않은 경우 방문 
        if currX >= 0 and currX < column and currY >= 0 and currY < row and graph[currY][currX] == 0 :
            dfs(graph, currY, currX) 

cnt = 0
for i in range(row) :
    for j in range(column) :
        if graph[i][j] == 0 :
            cnt += 1
            dfs(graph,i, j)

print(cnt)


    
    