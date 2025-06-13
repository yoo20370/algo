import sys 

INF = int(1e9)

def floyd() :
    node_count = int(sys.stdin.readline().rstrip())
    edge_count = int(sys.stdin.readline().rstrip())

    graph = [[INF] * (node_count + 1) for _ in range(node_count + 1)]
    for _ in range(edge_count) :
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start][end] = cost

    for i in range(1, node_count + 1) :
        graph[i][i] = 0

    for mid in range(1, node_count + 1) :
        for start in range(1, node_count + 1) :
            for end in range(1, node_count + 1) :
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

    for i in range(1, node_count + 1) :
        for j in range(1, node_count + 1) :
            print(graph[i][j], end=" ")
        print()
floyd()