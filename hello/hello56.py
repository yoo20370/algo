# bfs 
from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def dfs(graph, startNode) :

    queue = deque([startNode])
    visited = []

    while queue :
        currentNode = queue.popleft()

        if currentNode in visited :
            continue

        visited.append(currentNode)

        for adjacentNode in graph[currentNode] :
            if adjacentNode not in visited :
                queue.append(adjacentNode)

    return visited
def solution() :
    
    result = dfs(graph, 1)
    print(result)

solution()
