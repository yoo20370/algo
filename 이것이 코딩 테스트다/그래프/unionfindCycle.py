import sys 
def find_parent(parentTable, x) :
    if parentTable[x] != x :
        parentTable[x] = find_parent(parentTable, parentTable[x])
    return parentTable[x]

def union(parentTable, a, b) :
    pa = find_parent(parentTable, a)
    pb = find_parent(parentTable, b)
        
    if pa < pb :
        parentTable[pb] = parentTable[pa]
    else :
        parentTable[pa] = parentTable[pb]

v, e = map(int, sys.stdin.readline().split())

parent = [i for i in range(v+1)]

# edge
for _ in range(e) :
    start, end = map(int, sys.stdin.readline().split())
    if parent[start] == parent[end] :
        print("사이클이 발생했습니다.")
        break
    else :
        union(parent, start, end)

for i in range(1, v+1) :
    print(parent[i], end=" ")