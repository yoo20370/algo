import sys

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y) -> None :
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y :
        parent[y] = parent[x]
    else :
        parent[x] = parent[y]

def check_connection(parent,x, y) -> bool :
    if find_parent(parent, x) == find_parent(parent, y) :
        return True
    return False 

N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(N+1)]

for _ in range(M) :
    command, start, end = map(int, sys.stdin.readline().split())

    if command == 0 :
        if not check_connection(parent, start, end) :
            union(parent, start, end)
    elif command == 1 :
        if check_connection(parent, start, end) :
            print("YES")
        else :
            print("NO")
