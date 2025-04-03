import sys

INF = int(1e9)

node_count = int(sys.stdin.readline().rstrip())

edge_count = int(sys.stdin.readline().rstrip())

graph = [[INF] * (node_count + 1) for _ in range(node_count+1)]

for i in range(1, node_count+1) :
    graph[i][i] = 0

for _ in range(edge_count) :
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start][end] = cost

# 플로이드 워셜
# start, end로 직접 가는 것과 start mid end로 가는 모든 경우를 비교하여 최단 거리를 구한다. 없다면 INF로 놓는다. 

for mid in range(1, node_count+1) :
    for start in range(1, node_count+1) :
        for end in range(1, node_count+1) :
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])
        

for i in range(1, node_count+1) :
    for j in range(1, node_count+1) :
        print(graph[i][j], end=" ")
    print()
