# 플로이드 워셜이란 중간 정점을 순서대로 순회하며 출발지, 목적지 쌍에 대해 모두 비교하여 노드간 최소 경로를 구하는 알고리즘으로 알고 있음 

INF = int(1e9)

import sys 

def solution() :
    cityCount = int(sys.stdin.readline().rstrip())
    busCount = int(sys.stdin.readline().rstrip())

    graph = [[INF] * (cityCount + 1) for _ in range(cityCount + 1)]

    for city in range(1, cityCount + 1) :
        graph[city][city] = 0

    for _ in range(busCount) :
        begin, end, cost = map(int, sys.stdin.readline().split())
        graph[begin][end] = min(graph[begin][end], cost)
        
    for mid in range(1, cityCount + 1) :
        for begin in range(1, cityCount + 1) :
            for end in range(1, cityCount + 1) :
                graph[begin][end] = min(graph[begin][end], graph[begin][mid] + graph[mid][end])

    for currentRow in range(1, cityCount + 1) :
        for currentCol in range(1, cityCount + 1) :
            print(graph[currentRow][currentCol], end=" ")
        print()

solution()