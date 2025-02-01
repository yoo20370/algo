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

N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(N + 1)]

for _ in range(M) :

    command, a, b = map(int, sys.stdin.readline().split())

    if command == 0 :
        union(parent, a, b)
    elif command == 1 :
        if find_parent(parent, a) == find_parent(parent, b) :
            print("YES")
        else :
            print("NO")

