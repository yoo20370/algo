import sys
from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]


def bfs(start) -> None : 

    visited = [False] * 9
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue :
        curr_node = queue.popleft()
        print(curr_node, end=" ")

        for node in graph[curr_node] :
            if not visited[node] :
                visited[node] = True
                queue.append(node)

bfs(1)