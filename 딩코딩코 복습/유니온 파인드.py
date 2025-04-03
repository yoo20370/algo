import sys 

# 본인이 속한 집합을 찾으면서 갱신도 해주는 것 
# 시간 복잡도를 감소시킬 수 있음 
# 최고 조상을 찾을 때만 최고 조상이 갱신 되므로, 아직 갱신되지 않은 부분이 있을 수 있으므로 사요할 때 조심해서 사용할 것 
# 즉, 직접 parent[x]를 사용할 때 조심해야 한다. 
def find_parent(parent, x) -> int : # O(1)
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union 연산 
# 두 원소의 부모를 찾은 뒤 순서가 더 앞인 원소를 부모로 지정하여 두 집합을 하나로 합친다.
def union(parent, a, b) -> None :
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if a < b:
        parent[b] = parent_a
    else :
        parent[a] = parent_b

## 사이클 판별 
def check_cycle(parent, a, b) -> bool:
    if find_parent(parent, a) != find_parent(parent, b) :
        return False
    else :
        return True