import sys

INF = int(1e9)

companyCnt, routeCnt = map(int, sys.stdin.readline().split())

graph = [[INF] * (companyCnt +1) for _ in range(companyCnt + 1)]

for i in range(routeCnt) :
    startPoint, endPoint = map(int, sys.stdin.readline().split())
    graph[startPoint][endPoint] = 1
    graph[endPoint][startPoint] = 1

endPoint, midPoint = map(int, sys.stdin.readline().split())

for i in range(1, companyCnt + 1) :
    graph[i][i] = 0 

def floyd(graph) :
    for mid in range(1, companyCnt + 1) :
        for start in range(1, companyCnt + 1) : 
            for end in range(1, companyCnt + 1) :
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

floyd(graph)

result = graph[1][midPoint] + graph[midPoint][endPoint]
if result >= INF :
    print(-1)
else :
    print(result)

