# ㄷㄷ vlogv 다익스트라 시간초과 -> O(V + E) BFS ???? 

# 1 ~ N번까지 도시와 
## M개의 단방향 도로가 존재
## 모든 도로의 거리는 1이다. 

## 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중
## 최단 거리가 모두 K인 도시를 출력하는 프로그램을 작성하시오 

# 다익스트라 사용하라는 의미 
# INF, 최단 거리 테이블을 만들고 INF로 모두 초기화
# priority_queue에 출발 도시를 넣고, 0으로 초기화한다.

# priority_queue에서 도시 하나를 꺼내고, 인접한 도시의 최단거리를 구해서 최단 거리 테이블을 갱신한다.
# priority_queue 크기가 0이 될때까지 반복한다.

# 최단 거리 테이블을 순회하면서, K인 도시를 출력한다.

import sys, heapq

INF = int(1e9)

def solution() :
    city_count, load_count, distance_info, start_city = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(city_count + 1)]

    for _ in range(load_count) :
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)

    shortest_distance_table = [INF for _ in range(city_count + 1)]

    priority_queue = []
    heapq.heappush(priority_queue, (start_city, 0))
    shortest_distance_table[start_city] = 0

    while priority_queue :
        curr_city, curr_distance = heapq.heappop(priority_queue)

        # 이미 방문한 경우 
        if shortest_distance_table[curr_city] < curr_distance :
            continue

        for nearby_city in graph[curr_city] :
            nearby_distance = curr_distance + 1
            if shortest_distance_table[nearby_city] > nearby_distance :
                shortest_distance_table[nearby_city] = nearby_distance
                heapq.heappush(priority_queue, (nearby_city, nearby_distance))
    
    result_list = []
    for index in range(1, len(shortest_distance_table)):
        if shortest_distance_table[index] == distance_info :
            result_list.append(index)

    if len(result_list) == 0 :
        print(-1)
    else :
        for city in result_list :
            print(city)

solution()