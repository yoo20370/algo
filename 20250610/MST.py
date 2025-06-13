# 프림 알고리즘 
import sys, heapq

# def prim_algo() :
#     visited = []
#     city_count, road_count = map(int, sys.stdin.readline().split())

#     graph = [[] * (city_count + 1) for _ in range(city_count + 1)]

#     for _ in range(road_count) :
#         start, end, cost = map(int, sys.stdin.readline().split())
#         graph[start].append([cost, end])

#     priority_queue = []
#     heapq.heappush(priority_queue, [0, 1])

#     total_cost = 0
#     while priority_queue :
#         curr_cost, curr_city = heapq.heappop(priority_queue)

#         if curr_city in visited :
#             continue 
#         visited.append(curr_city)
#         total_cost += curr_cost

#         for next_cost, next_city in graph[curr_city] :
#             if next_city not in visited :
#                 heapq.heappush(priority_queue, [next_cost, next_city])
    
#     print(total_cost)

# prim_algo()

# 크루스칼 알고리즘
def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y) :
    parent_x = find(parent, x)
    parent_y = find(parent, y)

    if parent_x < parent_y :
        parent[parent_y] = parent_x
    else :
        parent[parent_x] = parent_y 

def kuruskal() :
    city_count, road_count = map(int, sys.stdin.readline().split())

    road_list = []
    for _ in range(road_count) :
        start, end, cost = map(int,sys.stdin.readline().split())
        road_list.append([cost, start, end])
    
    road_list.sort(key = lambda x : x[0])

    parent = [i for i in range(city_count + 1)]

    total_cost = 0
    for curr_cost, curr_stsrt, curr_end in road_list :
        # 사이클 없음 
        if find(parent, curr_stsrt) != find(parent, curr_end) :
            union(parent, curr_stsrt, curr_end)
            total_cost += curr_cost
    
    print(total_cost)
            
kuruskal()