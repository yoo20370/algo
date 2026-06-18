import sys
from itertools import combinations

INF = int(1e9)

def cal_chicken_distance(x1, y1, x2, y2) :
    return abs(x1 - x2) + abs(y1 - y2)

def total_cost(house_list, chicken_list) :

    total_cost = 0
    for x1, y1 in house_list :
        
        min_cost = INF
        for x2, y2 in chicken_list :
            min_cost = min(min_cost, cal_chicken_distance(x1,y1, x2,y2))
        
        total_cost += min_cost

    return total_cost

def chicken_delivery() :

    N, M = map(int, sys.stdin.readline().split())

    chicken_map = []
    for _ in range(N) :
        chicken_map.append(list(map(int, sys.stdin.readline().split())))


    house_list = []
    chicken_list = []
    for i in range(N) :
        for j in range(N) :
            if chicken_map[i][j] == 1 :
                house_list.append((i,j))
            elif chicken_map[i][j] == 2 :
                chicken_list.append((i,j))
    
    select_chicken_list = []
    for x in combinations(chicken_list, M) :
        select_chicken_list.append(x)

    min_distance = INF
    for select_list in select_chicken_list :
        result = total_cost(house_list, select_list) 
        min_distance = min(min_distance, result)

    return min_distance

print(chicken_delivery())

