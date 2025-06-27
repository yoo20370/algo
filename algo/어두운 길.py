# N개의 집과 M개의 도로로 구성
# 각 집은 0 ~ N - 1번까지 번호로 구분 

## 모든 도로에는 가로등 구비 
## 특정한 도로가의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일 
## 정부에서 일부 가로등을 비활성하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만 으로도 오갈 수 있도록 만들고자 함 
## 결과적으로 일부 가로등을 비활성하여 최대한 많은 금액을 절약하고자 한다.
## 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하세요'

#######################################333

## 크루스칼 알고리즘을 이용하려고 한다.
## 우선 도로 리스트를 만들고, 모든 비용을 합한 결과를 변수에 저장한다.
## 비용을 기준으로 내림차순 정렬을 수행한뒤 union-find 연산을 통해 사이클을 확인하며, 사이클이 발생하지 않으면 가로등 비용을 계산한다.

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

def solution() :
    house_count, street_lamp_count = map(int, sys.stdin.readline().split())

    total_cost = 0

    load_list = []
    for _ in range(street_lamp_count) :
        start, end, cost = map(int, sys.stdin.readline().split())
        load_list.append((start, end, cost))

        total_cost += cost
    
    load_list.sort(key=lambda x : x[2])

    parent = [i for i in range(house_count)]

    street_lamp_cost = 0
    for start, end, cost in load_list :
        if find(parent, start) != find(parent, end) :
            # 사이클이 존재하지 않음 
            union(parent, start,end)
            street_lamp_cost += cost

    
    print(total_cost - street_lamp_cost)

solution()

