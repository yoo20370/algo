# 단방향 그래프
# 특정 도시에서 다른 도시들로 전파해야 함 
# 이 때, 몇 개의 도시로 전보가 갔으며 시간은 어느 정도 걸렸는지 체크 

# 힙에, 시작 도시를 넣는다. 
# 최단 거리 테이블의 시작 도시 값을 0으로 설정한다. 
# 힙에서 가장 최단 거리를 갖는 도시를 꺼낸다. 
# 최단 거리 테이블의 값과 비교했을 때, 꺼낸 최단거리가 더 짧다면, 전파된 도시 개수를 카운트한다. 
# 전파된 도시의 최단 거리와 인접한 도시로의 이동 거리 합이 최단 거리 테이블의 도시 값보다 작다면, 최단 거리를 갱신하고, 힙에 넣는다. 
# 더 이상 반복문이 실행되지 않는다면, 최단 거리 테이블에서 값이 가장 큰 도시의 값을 선택하면 된다. 
import sys, heapq

INF = int(1e9)

city_cnt, route_cnt, start_city = map(int, sys.stdin.readline().split())

graph = [[] for i in range(city_cnt + 1)]
for _ in range(route_cnt) :
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append((end, time))

def send_signal(city_cnt, start_city, graph) -> None :

    heap = []
    times = [INF for _ in range(city_cnt + 1)]
    times[start_city] = 0
    heapq.heappush(heap, (times[start_city], start_city))

    visited_city_cnt = 0

    while heap :
        curr_time, curr_city = heapq.heappop(heap)

        if times[curr_city] < curr_time :
            continue

        visited_city_cnt += 1 

        for end_city, end_city_time in graph[curr_city] :
            temp_time = end_city_time + curr_time
            if times[end_city] > temp_time :
                times[end_city] = temp_time
                heapq.heappush(heap, (temp_time, end_city))
    
    total_time = max([t for t in times if t != INF])

    print(visited_city_cnt - 1, total_time) 

send_signal(city_cnt, start_city, graph)

