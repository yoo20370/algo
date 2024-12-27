import sys
sys.setrecursionlimit(int(1e5))

cnt = 1

def dfs(graph, visited, node) -> None:
    global cnt
    visited[node] = cnt
    
    for curr in graph[node] :
        if visited[curr] == 0 :
            cnt += 1
            dfs(graph, visited, curr)

node, edge, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(node+1)]

visited = [0] * (node + 1)

for _ in range(edge) :
    start_node, end_node = map(int, sys.stdin.readline().split())
    graph[start_node].append(end_node)
    graph[end_node].append(start_node)

for i in range(1, node+1) :
    graph[i].sort()

dfs(graph, visited, start)

for i in range(1, node+1) :
    print(visited[i])