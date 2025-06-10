import sys

INF = int(1e9)

v = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())

graph = [ [INF] * (v+1) for _ in range((v+1))]

for i in range(1, v+1) :
    graph[i][i] = 0

for _ in range(e) :
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start][end] = cost


def floyd(graph) :

    for mid in range(1, v+1) :
        for start in range(1, v+1) :
            for end in range(1, v+1) :
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])
floyd(graph)

for i in range(1, v+1) :
    for j in range(1, v+1) :
        print(graph[i][j], end=" ")
    print()