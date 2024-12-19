import sys

INF = int(1e9)

companyCnt, routeCnt = map(int, sys.stdin.readline().split())

graph = [[INF] * (companyCnt + 1) for i in range(companyCnt + 1)]

for idx  in range(1, companyCnt + 1) :
    graph[idx][idx] = 0

for _ in range(routeCnt) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start][end] = 1
    graph[end][start] = 1

startPoint = 1
endPoint, K = map(int, sys.stdin.readline().split()) 

def floyd() -> None :
    for mid in range(1, companyCnt + 1) :
        for start in range(1, companyCnt + 1) :
            for end in range(1, companyCnt + 1) :
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

floyd()

result = graph[startPoint][K] + graph[K][endPoint]
if result >= INF :
    print(-1)
else :
    print(result)

