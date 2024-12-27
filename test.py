import sys



def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = parent[a]
    else :
        parent[a] = parent[b]

def func() -> int :
    N, M = map(int, sys.stdin.readline().split())

    parent = [i for i in range(N+1)]
    graph = []

    for _ in range(M) :
        start, end = map(int, sys.stdin.readline().split())
        graph.append([start, end])

    cnt = 0
    for start, end in graph :
        if find_parent(parent, start) != find_parent(parent, end) :
            union(parent, start, end)
            cnt += 1

    return cnt

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    print(func())
