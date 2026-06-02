import sys
INF = int(1e9)

def solution() :
    companyCount, routeCount = map(int, sys.stdin.readline().split())

    graph = [[INF] * (companyCount + 1) for _ in range(companyCount + 1)]

    for i in range(1, companyCount + 1) :
        graph[i][i] = 0

    for _ in range(routeCount) :
        start, end = map(int, sys.stdin.readline().split())
        graph[start][end] = 1
        graph[end][start] = 1
    
    startCompany = 1
    endCompany, stopoverCompany = map(int, sys.stdin.readline().split())

    for stopover in range(1, companyCount + 1) :
        for start in range(1, companyCount + 1) :
            for end in range(1, companyCount + 1) :
                graph[start][end] = min(graph[start][end], graph[start][stopover] + graph[stopover][end])
    
    # 1번 회사 - 출발지 
    # X - 방문할 회사 (목적지)
    # K - 거쳐야 하는 회사

    distance = graph[startCompany][endCompany] + graph[stopoverCompany][endCompany]

    if distance >= INF :
        print(-1)
    else :
        print(distance)

solution()

# 생각을 해보자 나는 어떤 생각이었냐면 
# 결국 모든 최단 거리를 구하는 거임 
# 그 다음 출발지에서 경유지로, 경유지에서 목적지로 이동하는 거리의 합을 구하는거임 
# 그러면 반드시 최단거리가 될거잖아 ?? 
# 그래서 플로이드 워셜 돌린 다음에 처리하려고 마지막에 더해서 결과 내려고 했음 