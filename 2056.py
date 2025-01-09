import sys
from collections import deque 

n = int(sys.stdin.readline().rstrip())

m = int(sys.stdin.readline().rstrip())

graph = [ [] for _ in range(n+1)]

for _ in range(m) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (n+1)

cnt = 0 
def bfs() :
    cnt = 0

    queue = deque()
    queue.append((1, 0))
    visited[1] = True

    while queue :
        node, deepth = queue.popleft()
        if deepth <= 2 :
            cnt += 1

        for curr in graph[node] :
            if visited[curr] == False : 
                visited[curr] = True
                queue.append((curr, deepth +1))

    print(cnt - 1)
bfs()