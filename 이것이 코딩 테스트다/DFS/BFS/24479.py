import sys
sys.setrecursionlimit(int(1e5))



def dfs(graph, visited, node) -> None:
    
    visited[node] = True
    print(node)
    
    for curr in graph[node] :
        if visited[curr] == False :
            dfs(graph, visited, curr)

node, edge, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(node+1)]

visited = [0] * (node + 1)

for _ in range(edge) :
    start_node, end_node = map(int, sys.stdin.readline().split())
    graph[start_node].append(end_node)
    graph[end_node].append(start_node)

dfs(graph, visited, start)
