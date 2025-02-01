import sys 

def find_parent(parent, x) -> int :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b) -> None :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 더 작은 인덱스가 부모로 하는 것이 관례 
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, sys.stdin.readline().split())

parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    union(parent, a, b)

# for i in range(v+1) :
#     print(find_parent(parent, i), end=' ')

# print()

for i in parent :
    print(i, end=" ")

