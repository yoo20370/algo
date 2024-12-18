import sys

INF = int(1e9)

node, edge = map(int, sys.stdin.readline().split())

graph = [[INF] * (node + 1) for _ in range(node+1)]

for i in range(1, node + 1) :
    graph[i][i] = 0

for _ in range(edge) :
    startNode, endNode, cost = map(int, sys.stdin.readline().split())
    graph[startNode][endNode] = cost

def floyd() -> None :
    for mid in range(1, node+1) :
        for start in range(1, node+1) :
            for end in range(1, node+1) :
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

floyd()

for i in range(1, node+1) :
    for j in range(1, node+1) :
        print(graph[i][j], end=" ")
    print()