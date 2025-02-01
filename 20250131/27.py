import sys

INF = int(1e9)

node = int(sys.stdin.readline().rstrip())

edge = int(sys.stdin.readline().rstrip())

map_ = [[INF] * node for _ in range(node) ]

for i in range(node) :
    map_[i][i] = 0 

for _ in range(edge) :
    start_node, end_node, cost = map(int, sys.stdin.readline().split())
    map_[start_node-1][end_node-1] = cost

for mid in range(node) :
    for start in range(node) :
        for end in range(node) :
            map_[start][end] = min(map_[start][end], map_[start][mid] + map_[mid][end])

for i in range(node) :
    for j in range(node) :
        print(map_[i][j], end=" ")
    print()