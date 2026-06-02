import sys

INF = int(1e9)

def solution() :

    nodeCount = int(sys.stdin.readline().rstrip())
    edgeCount = int(sys.stdin.readline().rstrip())

    graph = [[INF] * (nodeCount + 1) for _ in range(nodeCount + 1) ]

    for i in range(1, nodeCount + 1) :
        graph[i][i] = 0
    
    for _ in range(1, edgeCount + 1) :
        startNode, endNode, cost = map(int, sys.stdin.readline().split())
        graph[startNode][endNode] = cost

    
    for stopover in range(1, nodeCount + 1) :
        for start in range(1, nodeCount + 1) :
            for end in range(1, nodeCount + 1) :
                graph[start][end] = min(graph[start][end], graph[start][stopover] + graph[stopover][end])

    for row in range(1, nodeCount + 1) :
        for col in range(1, nodeCount + 1) :
            print(graph[row][col], end = " ")
        print()
                

solution()