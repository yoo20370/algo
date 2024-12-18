import sys
from collections import deque

row, column = map(int, sys.stdin.readline().split())

graph = []

for i in range(row) :
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

N = row - 1
M = column - 1

start = 0
end = 0

# 동, 서, 남, 북
check = [(1,0), (-1,0), (0, 1), (0, -1)]

def miroEscape(graph, x, y) -> None:
    queue = deque()
    queue.append([x,y])
    graph[y][x] = 1

    while queue :
        currX, currY = queue.popleft()

        for dx, dy in check :
            nx = currX + dx
            ny = currY + dy
            if nx >= 0 and nx <= M and ny >= 0 and ny <= N and graph[ny][nx] == 1 :
                # 방문처리
                graph[ny][nx] = graph[currY][currX] + 1
                queue.append([nx, ny])
                if ny == N and nx == M :
                    print(graph[ny][nx])
                    break

miroEscape(graph, start, end)

