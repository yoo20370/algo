
graph = [
    [],
    [2,3],
    [4,5],
    [6,7],
    [],
    [],
    [],
    []
]

visited = [False] * len(graph)

stack = list()

def dfs(curr, visited) :

        # 방문처리 
        visited[curr] = True
        print(curr)
        for node in graph[curr] :
            if visited[node] == False :
                dfs(node, visited)

dfs(1, visited)