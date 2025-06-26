# 한울이가 사는 나라에는 N개의 여행지가 있다. 1 ~ N번까지의 번호로 구분 
# 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존해할 수 있다. 
# 이때 여행지가 도로로 연결되어 있다면, 양방향 이동이 가능 (양방향 그래프)

# 한울이는 하나의 여행 계획을 세운 뒤, 이 여행 계획이 가능한지의 여부를 판단하고자 함 
# 한울이는 하나의 여행계획을 세운 뒤 이 여행 계획이 가능한지 여부를 판단하고자 한다
# N이 5일 때, 
# 도로 정보 
# 1 - 2
# 1 - 4
# 1 - 5
# 2 - 3
# 2 - 4

# 한울이 계획 2 -> 3 -> 4 -> 3 
# 2 -> 3 -> 2 -> 4 -> 2 -> 3 방문하면 계획 따를 수 있음 

##################
# 어떻게 풀거야 ??
# 2 -> 3 -> 2 -> 4 -> 2 -> 3 방문하면 가능 -> 이말은 즉 서로 연결되어 있으면 된다는 의미 즉, union-find를 사용해야한다는 의미
# 항상 모르겠으면 내가 예제를 어떻게 머리로 생각해냈는지 고민해봐라 

import sys

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y) :
    x_parent = find(parent, x)
    y_parent = find(parent, y)

    if x_parent < y_parent :
        parent[y_parent] = x_parent
    else :
        parent[x_parent] = y_parent

def cycle_check(parent, x, y) :
    if find(parent, x) != find(parent, y) :
        return False
    return True

def solution() :
    tour_spot_count = int(sys.stdin.readline().rstrip())
    plan_tour_spot_count = int(sys.stdin.readline().rstrip())


    set_table = [i for i in range(tour_spot_count)]

    graph = []
    for _ in range(tour_spot_count) :
        graph.append(list(map(int , sys.stdin.readline().split())))

    plan_tour_spot_list = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
    
    for i in range(tour_spot_count) :
        for j in range(tour_spot_count) :
            if graph[i][j] == 1 :
                # 같은 집합이 아니라면 
                if not cycle_check(set_table, i, j) :
                    union(set_table, i, j)

    # 부모가 다르면 같은 집합이 아님 
    result = find(set_table, plan_tour_spot_list[0])
    for index in range(1, len(plan_tour_spot_list)) :
        if result != find(set_table, plan_tour_spot_list[index]) :
            return "NO"

    return "YES"

print(solution())