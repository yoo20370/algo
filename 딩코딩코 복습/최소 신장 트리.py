import sys
# 크루스칼 알고리즘
# 간선 정보를 비용을 기준으로 오름차순 정렬한다.
# 간선 정보를 활용했을 때, 기존 집합이 사이클이 존재하는지 파악한다.
# 사이클이 존재하지 않는다면 union한다. 존재한다면 넘어간다. 

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

node_cnt, edge_cnt = map(int, sys.stdin.readline().split())

edges = []
for _ in range(edge_cnt) :
    edges.append(list(map(int, sys.stdin.readline().split())))

edges.sort(key=lambda x : (x[2]))

parent = [i for i in range(node_cnt + 1)]

total_cost = 0
for start, end, cost in edges :
    if find_parent(parent, start) != find_parent(parent, end) :
        union(parent, start, end)
        total_cost += cost

print(total_cost)


