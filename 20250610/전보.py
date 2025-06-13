# 도시 C에서 출발하여 다른 도시로 전보를 전달 -> 메시지를 받게되는 도시의 개수와 걸리는 시간을 계산
# 특정 노드에서 다른 노드로의 최단 거리를 구하는 문제 -> 다익스트라 최단 거리 알고리즘 사용
# 언제 메시지 받은 도시 개수 카운트 ?? -> 우선순위 큐에서 꺼냈을 때, 아직 한 번도 최단거리를 구하지 않은 경우 카운트 
# 걸리는 시간은 ?? -> 모두 탐색한 후, time_table을 순회하면서 가장 오래 걸린 시간을 찾는다. 

import sys, heapq

INF = int(1e9)

def send_message() :
    city_count, route_count, start_city = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(city_count + 1)]

    for _ in range(route_count) :
        begin_city, destination_city, time = map(int, sys.stdin.readline().split())
        graph[begin_city].append([time, destination_city])

    time_table = [INF] * (city_count + 1)
    priority_queue = []

    heapq.heappush(priority_queue, [0, start_city])
    time_table[start_city] = 0

    count = 0
    while priority_queue :
        curr_time, curr_city = heapq.heappop(priority_queue)

        if time_table[curr_city] < curr_time :
            continue
        # 최단시간 측정한 적 없음, 그러므로 최단시간 최초 측정이므로 방문 도시 up
        count += 1

        for near_time, near_city in graph[curr_city] :
            min_time = curr_time + near_time

            if time_table[near_city] > min_time :
                time_table[near_city] = min_time
                heapq.heappush(priority_queue, [min_time, near_city])
                
    take_time = 0
    for i in range(1, city_count + 1) :
        if time_table[i] != INF and take_time < time_table[i] :
            take_time = time_table[i]
    
    # 시작 도시에 대해서도 카운트했기 때문에 1을 빼준다.
    print(count - 1, take_time)
send_message()