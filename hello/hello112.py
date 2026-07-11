# N개의 여행지가 있다 
# 각 여행지는 1 ~ N까지의 번호로 구분된다.
# 도로가 연결되어 있다면 양방향 
# 하나의 여행 계획을 세운 뒤, 이 여행 계획이 가능한지 여부를 판단하고자 함 
# 결국 하나의 집합 즉, 특정 위치로 가는 간선이 존재하는지 묻는 문제 같음 
# dfs를 통해서 탐색할 수도 있다고 생각 

# 그러면 결국 edge를 기록하고 
# union-find를 통해서 집합을 만들고 같은 집합인지 확인 하는 방법을 취해야 할 것 같음 

# 일단 어떻게 edge를 다루면 좋을까 ?? 그냥 추가적인 데이터 저장 없이 입력값이 들어오면 그 입력값을 바로 다뤄서 union-find를 진행할까 ??
# 굳이 저장할 필요는 없을 것 같은데 이후 추가적으로 사용되지 않음 그냥 입력값이 들어올 떄 바로바로 처리하는게 좋을 것 같음 
import sys

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y ) :
    parentX = find(parent, x)
    parentY = find(parent, y)

    if parentX < parentY :
        parent[parentY] = parentX
    else :
        parent[parentX] = parentY

def solution() :
    travelDestinationCount, travelCityCount = map(int, sys.stdin.readline().split())

    parent = [i for i in range(travelDestinationCount + 1)]

    for beginTravelCity in range(1, travelDestinationCount + 1) :
        loadList = list(map(int, sys.stdin.readline().split()))

        for endTravelCity in range(1, travelDestinationCount + 1) :
            endTravelCityIndex = endTravelCity - 1
            if loadList[endTravelCityIndex] == 1 :
                if find(parent, beginTravelCity) != find(parent, endTravelCity) :
                    union(parent, beginTravelCity, endTravelCity)

    
    travelRoute = list(map(int, sys.stdin.readline().split()))

    for travelCity in range(1, travelDestinationCount + 1) :
        find(parent, travelCity)

    compareCity = parent[travelRoute[0]]
    for travelCity in travelRoute: 
        if parent[travelCity] != compareCity :
            return "NO"
    
    return "YES"

print(solution())