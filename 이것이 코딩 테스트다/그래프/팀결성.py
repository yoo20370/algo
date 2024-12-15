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
 
N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(N+1)]

for i in range(M) :
    commands, first, second = map(int, sys.stdin.readline().split())

    if commands == 0 :
        union(parent, first, second)
    elif commands == 1 :
        if parent[first] == parent[second] :
            print("YES")
        else :
            print("NO")
    
