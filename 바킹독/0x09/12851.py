# 비슷한 유형의 문제에서 0에서 100,000 사이에서만 움직인다고 멋대로 가정하면 안 된다.
# 이 문제의 경우는 운 좋게 이 가정이 잘 들어 맞은 것 
import sys
from collections import deque

MX = 100005

INF = int(1e9)

# 방문처리를 위한 배열 
graph = [INF] * MX

N, K = map(int, sys.stdin.readline().split())

# bfs에서 사용할 큐 
queue = deque()
queue.append(N)
graph[N] = 0

while queue :
    curr = queue.popleft()

    # 처음에 계산된 값이 최소값이므로 한 번만 계산해주면 된다.
    if curr - 1 >= 0 :
        if graph[curr-1] == INF :
            graph[curr-1] = graph[curr] + 1
            queue.append(curr-1)

    if curr + 1 < MX :
        if graph[curr+1] == INF :
            graph[curr+1] = graph[curr] + 1
            queue.append(curr+1)

    if curr * 2 < MX :
        if graph[curr*2] == INF :
            graph[curr*2] = graph[curr] + 1
            queue.append(curr*2)
        
print(graph[K])


