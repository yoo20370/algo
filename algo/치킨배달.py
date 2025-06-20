# N * N 도시 
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나 
# 도시의 칸은 (r, c) 형태로 나타냄 

# 치킨 거리란 집과 가장 가까운 치킨 집 사이의 거리 
# 각각의 집은 치킨 거리가 있다. 
# 모든 집의 치킨 거리의 합 

# 0 -> 빈칸, 1-> 집, 2 -> 치킨집
# M개가 치킨집 최대 개수 

# 도시의 치킨집 중 최대 M개를 고르고, 나머지 치킨집은 모두 폐업 시켜야 한다. 어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오 

###################################

# 어떻게 해야할까 
# 그냥 단순하게 전역탐색을 하는게 맞을 것 같아 
# 예를 들어 집 리스트와 치킨집 리스트를 구한 다음에, 치킨 집을 조합을 이용해서 꺼낸다음 그 조합 리스트와 거리를 구하여 최단 거리를 구하면 되는거 아닌가 ?? 

# 가장 먼저 떠오른 것은 뭐냐면
# 일단, 집 리스트를 순회하면서, 접근 가능한 치킨 리스트와 모든 거리를 구한다음 최소값을 합계 거리에 추가한다. 
# 이 과정을 모든 집 리스트에 대하여, 모든 조합 리스트에 대하여 수행한다. 

import sys
from itertools import combinations

INF = int(1e9)

# 특정 위치에서 다른 위치까지의 거리를 계산하는 메서드 
def cal_chicken_distance(x1, y1, x2, y2) :
    return abs(x1 - x2) + abs(y1 - y2)

# 정해진 치킨집 M개에 대하여 치킨 거리를 구하는 메서드 
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

