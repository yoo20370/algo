from collections import deque

# graph = [
#     [],
#     [2,3],
#     [1,4,5],
#     [1,6,7],
#     [2],
#     [2],
#     [3],
#     [3]
# ]

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

def bfs(start, graph) :
    visited = [False] * len(graph)

    queue = deque()
    queue.append(start)
    visited[start] = True
    

    while queue :
        curr = queue.popleft()

        print(curr, end=" ")
        for i in graph[curr] :
            if visited[i] == False :
                queue.append(i)
                visited[i] = True


bfs(1, graph)