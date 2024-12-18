import sys

# graph = [
#     [],
#     [2,3],
#     [4,5],
#     [6,7],
#     [],
#     [],
#     [],
#     []
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

visited = [False] * 9
def dfs(root, visited) :
    
    visited[root] = True
    print(root, end=" ")

    for child in graph[root] :
        if visited[child] == False :
            dfs(child, visited)

dfs(1, visited)