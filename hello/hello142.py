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