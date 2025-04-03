# 크루스칼 알고리즘을 이용해서 최소 신장 트리를 구한다.
# 그리고 비용이 가장 큰 길을 제거하여 비용을 줄인다. 

import sys

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x]) 
    return parent[x]

def union(parent, a, b) -> None :
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a < parent_b :
        parent[parent_b] = parent_a
    else :
        parent[parent_a] = parent_b

def check_cycle(parent, a, b) -> bool :
    if find_parent(parent, a) != find_parent(parent, b) :
        return False
    else :
        return True

house_cnt, road_cnt = map(int, sys.stdin.readline().split())

road_list = []
for _ in range(road_cnt) :
    start, end, cost = map(int, sys.stdin.readline().split())
    road_list.append((start, end, cost))


def divide_city(road_list, house_cnt) -> int :
    road_list.sort(key=lambda x : x[2])
    parent = [i for i in range(house_cnt+1)]

    total_cost = 0
    last = 0
    for start, end, cost in road_list :
        if not check_cycle(parent, start, end) :
            union(parent, start, end)
            total_cost += cost
            last = cost
    
    total_cost -= last

    return total_cost

print(divide_city(road_list, house_cnt))
