# 경로 압축을 하지 않을 경우 find 함수가 모든 노드를 확인하므로 비효율적으로 동작한다. 최대 O(V) - 최악의 경우
# 이 경우 전체 시간 복잡도가 O(VM)이 된다. // M은 union 연산의 개수 V는 find 연산의 개수 
# 경로 압축을 통해 시간복잡도를 개선할 수 있다. 
# 경로 압축 기법에 사용하면 루트 노드에 더 빠르게 접근 가능 
import sys

def find_parent(parentTable, x) :
    if parentTable[x] != x :
        parentTable[x] = find_parent(parentTable, parentTable[x])
    return parentTable[x]

def union(parentTable, a, b) :
    parentA = find_parent(parentTable, a)
    parentB = find_parent(parentTable, b)

    # 부모 크기가 작은게 우선이므로 
    if parentA < parentB :
        parentTable[parentB] = parentTable[parentA]
    else :
        parentTable[parentA] = parentTable[parentB]

# 예제에서는 5, 4
V, E = map(int, sys.stdin.readline().split())

parentTable = [ i for i in range(V+1)]

for edge in range(E) :
    start, end = map(int, sys.stdin.readline().split())
    union(parentTable, start, end)

for i in range(1, V+1) :
    print(find_parent(parentTable, i), end=" ")

print()

for i in range(1, V + 1) :
    print(parentTable[i], end=" ")