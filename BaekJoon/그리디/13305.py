import sys

def func(distance, store_cost, min_cost, city_count) -> int :
    total_cost = 0
    remain_feul = 0
    
    for curr in range(city_count):
        if remain_feul == 0 :
            if store_cost[curr] == min_cost : 
                total_cost += sum(distance[curr:]) * min_cost 
                remain_feul += sum(distance[curr:]) 
            else :
                next = curr + 1
                while store_cost[curr] < store_cost[next] and next < city_count - 1:
                    next += 1
                

N = int(sys.stdin.readline().rstrip())

distance = list(map(int, sys.stdin.readline().split()))
store_cost = list(map(int, sys.stdin.readline().split()))

min_cost = min(store_cost)

print(func(distance, store_cost, min_cost))
