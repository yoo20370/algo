# 무방향 그래프 사이클 체크는 서로소 집합을 이용하면 된다.

import sys 

def find(parent, x) :
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y) :
    parent_x = find(parent, x)
    parent_y = find(parent, y)

    if parent_x < parent_y :
        parent[parent_y] = parent_x
    else :
        parent[parent_x] = parent_y

def check_cycle() :

    node_count, edge_count = map(int, sys.stdin.readline().split())
    parent_table = [i for i in range(node_count + 1)]

    for _ in range(edge_count) :
        start, end = map(int, sys.stdin.readline().split())

        if find(parent_table, start) != find(parent_table, end ):
            union(parent_table, start, end)
        else :
            return "사이클이 발생했습니다."

print(check_cycle())