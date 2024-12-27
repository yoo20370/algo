import sys 

N = int(sys.stdin.readline().rstrip())

visited = [False] * (N+1)

graph = [[] for i in range(N+1)]

def dfs(visited, node) :
    stack = list()

    visited[node] = True
    stack.append(node)

    while stack :
        curr = stack.pop()
        print(curr)

        for next in graph[curr] :
            if visited[next] == False :
                stack.append(next)
