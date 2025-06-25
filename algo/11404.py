# n개의 도시가 있다.
# 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다. 
# 각 버스는 한 번 사용할 때 필욯나 비용이 있다.

## 모든 도시의 쌍 (A,B)에 대해서 도시 A에서 b로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
## 가지 못하는 곳은 0으로 출력 

import sys 

INF = int(1e9)

def solution():
    city_count = int(sys.stdin.readline().rstrip())
    bus_count = int(sys.stdin.readline().rstrip())

    graph = [[INF] * city_count for _ in range(city_count)]

    for _ in range(bus_count) :
        begin, destination, cost = map(int, sys.stdin.readline().split())
        
        if graph[begin-1][destination-1] > cost :
            graph[begin-1][destination-1] = cost

    for i in range(city_count) :
        graph[i][i] = 0 

    for mid in range(city_count) :
        for begin in range(city_count) :
            for destination in range(city_count) :
                graph[begin][destination] = min(graph[begin][destination], graph[begin][mid] + graph[mid][destination])
    
    for i in range(city_count) :
        for j in range(city_count) :
            if graph[i][j] == INF and i != j:
                print("0", end=" ")
            else :
                print(graph[i][j], end =" ")
        print()

solution()