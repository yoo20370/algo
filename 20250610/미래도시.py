import sys

INF = int(1e9)

def future_city() :
    company_count, route_count = map(int, sys.stdin.readline().split())

    graph = [[INF] * (company_count + 1) for _ in range(company_count + 1)]

    for _ in range(route_count) :
        start, end = map(int, sys.stdin.readline().split())
        graph[start][end] = 1
        graph[end][start] = 1

    X, K = map(int,sys.stdin.readline().split())

    for i in range(1, company_count + 1):
        graph[i][i] = 0

    for mid in range(1, company_count + 1) :
        for start in range(1, company_count + 1) :
            for end in range(1, company_count + 1) :
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

    time = graph[1][K] + graph[K][X]
    if time >= INF :
        print(-1)
    else :
        print(time)

future_city()