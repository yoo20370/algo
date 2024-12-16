import sys
sys.setrecursionlimit(10**5)

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y) :
    # x의 부모를 찾는다.
    xp = find_parent(parent, x)
    # y의 부모를 찾는다.
    yp = find_parent(parent, y)

    # 노드 번호가 작은 것을 더 부모 결정하기 위함 
    if xp < yp :
        parent[yp] = parent[xp]
    else :
        parent[xp] = parent[yp] 

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)]

for _ in range(m) :
    command, a, b = map(int, sys.stdin.readline().split())

    if command == 0 :
        union(parent, a, b)
    else :
        if find_parent(parent, a) == find_parent(parent, b) :
        #if parent[a] == parent[b] :
            print("YES")
        else :
            print("NO")

