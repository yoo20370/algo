from collections import deque

# bfs
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# queue를 이용한 bfs
def solution(graph, startNode) :

    queue = deque([startNode])
    visited = list()

    while queue :
        currentNode = queue.popleft()

        if currentNode in visited :
            continue

        visited.append(currentNode)

        for adjacentNode in graph[currentNode] :
            if adjacentNode not in visited :
                queue.append(adjacentNode)

    print(visited)
solution(graph, 1)
