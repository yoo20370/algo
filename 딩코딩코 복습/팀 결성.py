# 유니온 파인드 연산을 수행하면 될 것 같다.
import sys

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) -> None :
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_b < parent_a :
        parent[parent_a] = parent_b
    else :
        parent[parent_b] = parent_a

N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(N+1)]
for _ in range(M) :
    command, a, b = map(int, sys.stdin.readline().split())

    if command == 0 :
        union(parent, a, b)
        
    elif command == 1 :
        if find_parent(parent, a) == find_parent(parent, b) :
            print("YES")
        else :
            print("NO")

