import sys

INF = int(1e9)
# 1 -> X 까지 가는 것 
# K 회사에 소개팅 상대가 있어서 들러야 한다.
# 1 -> K -> X

company_cnt, route_cnt = map(int, sys.stdin.readline().split())

map_data = [[INF] * (company_cnt + 1) for _ in range(company_cnt + 1)]

for i in range(1, company_cnt + 1) :
    map_data[i][i] = 0

for _ in range(route_cnt) :
    start, end = map(int, sys.stdin.readline().split())
    map_data[start][end] = 1
    map_data[end][start] = 1

X, K = map(int, sys.stdin.readline().split())

for mid in range(1, company_cnt + 1) :
    for start in range(1, company_cnt + 1) :
        for end in range(1, company_cnt + 1) :
            map_data[start][end] = min(map_data[start][end], map_data[start][mid] + map_data[mid][end])

distance = map_data[1][K] + map_data[K][X]

if distance >= INF :
    print(-1)
else :
    print(distance)
    