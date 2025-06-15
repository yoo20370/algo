import sys 
sys.setrecursionlimit(int(1e9))

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

def mst() :
    node_count, edge_count = map(int, sys.stdin.readline().split())

    edge_list = []

    for _ in range(edge_count) :
        start, end, cost = map(int, sys.stdin.readline().split())
        edge_list.append((cost, start, end))

    edge_list.sort(key=lambda x : x[0])

    parent = [i for i in range(node_count + 1)]

    total_cost = 0
    for cost, start, end in edge_list :
        if find(parent, start) != find(parent, end) :
            union(parent, start, end)
            total_cost += cost

    print(total_cost)

mst()




