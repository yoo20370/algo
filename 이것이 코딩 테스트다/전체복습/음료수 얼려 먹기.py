import sys

row, column = map(int, sys.stdin.readline().split())

graph = []

# 동, 서, 남, 북 y, x
check = [(1,0), (-1, 0),(0,1),(0,-1)]


for i in range(row) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(graph, y, x) :

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


    
    