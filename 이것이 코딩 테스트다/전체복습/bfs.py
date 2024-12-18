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

visited = [False] * 9

def bfs(node) :

    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue :
        curr = queue.popleft()
        print(curr, end=" ")

        for i in graph[curr] :
            if visited[i] == False :
                visited[i] = True
                queue.append(i)

bfs(1)