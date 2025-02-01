import sys 

INF = int(1e9)

company_cnt, road_cnt = map(int, sys.stdin.readline().split())

graph = [[INF] * (company_cnt + 1) for i in range(company_cnt + 1)]

for i in range(1, company_cnt + 1) :
    graph[i][i] = 0

for _ in range(road_cnt) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = 1
    graph[end][start] = 1

end_destination, mid_destination = map(int, sys.stdin.readline().split())

for mid in range(1, company_cnt + 1) :
    for start in range(1, company_cnt + 1) :
        for end in range(1, company_cnt + 1) :
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])


distance = graph[1][mid_destination] + graph[mid_destination][end_destination]

if distance >= INF :
    print(-1)
else :
    print(distance)