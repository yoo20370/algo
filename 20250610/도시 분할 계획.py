# 크루스칼 알고리즘을 이용하면 최소 신장 트리를 구하고, 마지막으로 연결한 마을의 비용을 빼면 될 것 같다.
# 하지만 프림 알고리즘으로 풀어본다.
# 프림 알고리즘으로 최소 신장 트리를 구하면서, 연결될 떄 비용이 가장 큰 것을 찾는다.
# 그리고 최소 신장 트리를 만든 뒤, 비용이 가장 큰 값을 빼주면 될 것 같다. 

# 프림 알고리즘이 더 느려서 시간초과 발생 
# 그냥 크루스칼로 풀게욘....
import sys, heapq

# def city_div_plan() :
#     house_count, road_count = map(int, sys.stdin.readline().split()) 

#     visited = {}
#     priority_queue = []

#     graph = [[] for _ in range(house_count + 1)]
    
#     for _ in range(road_count) :
#         start, end, cost = map(int, sys.stdin.readline().split())
#         graph[start].append((cost, end))
#         graph[end].append((cost, start))
        
#     heapq.heappush(priority_queue, [0, 1])

#     max_cost = 0
#     total_cost = 0
#     while priority_queue :
#         curr_cost, curr_city = heapq.heappop(priority_queue)

#         if visited.get(curr_city) : 
#             continue
#         visited[curr_city] = True
#         total_cost += curr_cost
#         max_cost = max(curr_cost, max_cost)

#         for near_cost, near_city in graph[curr_city] : 
#             if not visited.get(near_city) :
#                 heapq.heappush(priority_queue, [near_cost, near_city])
                

#     print(total_cost - max_cost)

# city_div_plan()

def find(city_table, house) :
    if city_table[house] != house :
        city_table[house] = find(city_table, city_table[house])
    return city_table[house]

def union(city_table, houseA, houseB) :
    houseA = find(city_table, houseA)
    houseB = find(city_table, houseB)

    if houseA < houseB :
        city_table[houseB] = houseA 
    else :
        city_table[houseA] = houseB

def city_div_plan() :
    house_count, road_count = map(int, sys.stdin.readline().split()) 

    road_list = []

    for _ in range(road_count) :
        start, end, cost = map(int, sys.stdin.readline().split())
        road_list.append((cost, start, end))

    road_list.sort(key = lambda x : x[0])

    city_table = [i for i in range(house_count + 1)]

    total_cost = 0
    last_cost = 0

    for cost, start, end in road_list :

        if find(city_table, start) != find(city_table, end) :
            union(city_table, start, end)
            total_cost += cost
            last_cost = cost

    print(total_cost - last_cost)

city_div_plan()
        
