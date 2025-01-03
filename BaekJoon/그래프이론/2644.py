import sys
from collections import deque
def bfs(graph, visited, start) -> None :

    queue = deque()
    queue.append(start)
    visited[start] += 1

    while queue :
        curr = queue.popleft()

        for end in graph[curr] :
            if visited[end] == 0 :
                visited[end] = visited[curr] + 1
                queue.append(end)
    
N = int(sys.stdin.readline().rstrip())

graph = [ [] for _ in range(N+1)] 

first, second = map(int, sys.stdin.readline().split())

K = int(sys.stdin.readline().rstrip())

for _ in range(K) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)


visited = [0] * (N+1)

bfs(graph, visited, second)

if visited[first] == 0 :
    print(-1)
else :
    print(visited[first] - 1)
