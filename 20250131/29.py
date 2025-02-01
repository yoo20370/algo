import sys, heapq

INF = int(1e9)

city_cnt, road_cnt, start_city = map(int, sys.stdin.readline().split())

distance = [INF] * (city_cnt + 1)

graph = [ [] for _ in range(city_cnt + 1)]

for _ in range(road_cnt) :
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))


heap = list()
distance[start_city] = 0
heapq.heappush(heap,(0, start_city) )

cnt = 0
max_cost = 0
while heap :
    curr_cost, curr_city = heapq.heappop(heap)

    if distance[curr_city] < curr_cost :
        continue
    
    cnt += 1
    max_cost = max(max_cost, curr_cost)
    
    for end_city, end_cost in graph[curr_city] :
        temp_cost = end_cost + curr_cost
        if distance[end_city] > temp_cost :
            distance[end_city] = temp_cost
            heapq.heappush(heap, (temp_cost, end_city))
            
            

# 시작 도시 cnt 빼줘야 함 
print(cnt - 1, max_cost)


