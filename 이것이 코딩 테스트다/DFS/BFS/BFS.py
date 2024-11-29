from collections import deque

graph = [
    [],
    [2,3],
    [1,4,5],
    [1,6,7],
    [2],
    [2],
    [3],
    [3]
]

visited = [False] * len(graph)

def bfs(start, graph, visited) :
    queue = deque()
    queue.append(start)
    visited[start] = True
    print(start, end=" ")

    while queue :
        curr = queue.popleft()

        for i in graph[curr] :
            if visited[i] == False :
                queue.append(i)
                visited[i] = True
                print(i, end=" ")


bfs(1, graph, visited)