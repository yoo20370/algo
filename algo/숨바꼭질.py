# 동빈이는 술래로부터 잡히지 않도록 수음 곳을 찾고 있다. 
# 동빈이는 1 ~ N번 까지의 헛간 중에서 하나를 골라 숨을 수 있다. 
## 술래는 항상 1번 헛간에서 출발 
## 전체 맵에는 총 M개의 양방향 통로가 존재 (양방향 그래프구만)
# 하나의 통로는 서로 다른 두 헛간을 연결합니다. 
# 또한 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어진다. 

# 동빈이는 1번 헛간으로부터 최단 거리가 가장 멋 헛간이 가장 안전하다고 판단하고 있다. 
## 이때, 최단 거리의 의미는 지나야 하는 길의 최소 개수를 의미한다. (방문할 때마다 1씩 증가시켜야겠네)
## 동빈이가 숨을 헛간의 번호를 출력하는 프로그램을 작성해라 

##  첫 번째는 숨어야 하는 헛간 번호를 (동일한 거리면 헛간 번호가 더 작은 것 )
##  두 번째는 거리 
##  세 번째는 동일한 거리의 헛간 개수 출력 

############ 
# 화성 탐색이 딱 보고 BFS가 생각났다면, 이건 다익스트라 최단거리 알고리즘이 생각남

import sys, heapq

INF = int(1e9)

def solution() :
    hiden_space_count, route_count = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(hiden_space_count + 1)]
    for _ in range(route_count) :
        start, end = map(int, sys.stdin.readline().split())

        ## 양방향이기 때문 
        graph[start].append(end)
        graph[end].append(start)

    distance = [INF] * (hiden_space_count + 1)

    priority_queue = []
    heapq.heappush(priority_queue, (0, 1))
    distance[1] = 0

    while priority_queue : 
        curr_cost, curr_hiden_space = heapq.heappop(priority_queue) 

        if distance[curr_hiden_space] < curr_cost :
            
            continue
        
        for nearby_hiden_space in graph[curr_hiden_space] :
            temp_cost = curr_cost + 1
           
            if distance[nearby_hiden_space] > temp_cost :
                distance[nearby_hiden_space] = temp_cost
                heapq.heappush(priority_queue, (temp_cost, nearby_hiden_space))

    max_cost = 0
    for index in range(1, hiden_space_count + 1) :
        if distance[index] != INF :
            max_cost = max(max_cost, distance[index])
    
    # 반복문 하나로 할 수 있지만 존재하는 함수를 사용해봤다. 
    hidden_space_number = distance.index(max_cost)
    hidden_space_same_count = distance.count(max_cost)

    print(hidden_space_number, max_cost, hidden_space_same_count)

solution()