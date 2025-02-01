import sys

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) -> None :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, sys.stdin.readline().split())

parent = [i for i in range(v+1)]

for _ in range(e) :
    a, b = map(int, sys.stdin.readline().split())

    if find_parent(parent, a) != find_parent(parent, b) :
        union(parent, a, b)
    else :
        print("사이클이 발생했습니다.")
        break

