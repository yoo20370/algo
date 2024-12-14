import sys

INF = int(1e9)

N = int(sys.stdin.readline().rstrip())
V = int(sys.stdin.readline().rstrip())

distance = [ [INF] * (N + 1) for _ in range(N+1) ]
for i in range(1, N + 1) :
    distance[i][i] = 0

for _ in range(V) :
    startNode, endNode, cost = map(int, sys.stdin.readline().split())
    distance[startNode][endNode] = cost

def floyd(distance) :
    for mid in range(1, N+1) :
        for start in range(1, N+1) :
            for end in range(1, N+1) :
                distance[start][end] = min(distance[start][end], distance[start][mid] + distance[mid][end])
floyd(distance)

for row in range(1, N+1) :
    for column in range(1, N+1) :
        if distance[row][column] == INF :
            print("INFINITY", end=" ")
        else :
            print(distance[row][column], end=" ")
    print()