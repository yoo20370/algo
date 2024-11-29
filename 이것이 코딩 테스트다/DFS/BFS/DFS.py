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

visited = [False] * len(graph)

def dfs(curr, visited) :

    # 방문처리 
    visited[curr] = True
    print(curr)
    for node in graph[curr] :
        if visited[node] == False :
            dfs(node, visited)

dfs(1, visited)

