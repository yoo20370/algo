import sys

# 주의할 점, 경로 압축을 수행했지만 모든 최상위 부모가 기록되어 있는 것은 아님
# 그러므로 최상위 부모를 모두 출력하라고 할 때는 find_parent() 메서드를 개별적으로 돌려야 함 !!!!!

def find_parent(parent, x) :
    # 왜 ? -> parent 테이블에 대해서 본인 값을 가지고 있지 않으면 다른 부모가 있다는 것
    if parent[x] != x :
        # 그럼 현재 parent 테이블에서 가리키는 노드의 부모를 찾으러 간다. 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# x와 y에 대하여 하나의 집합에 속하도록 만들어줘야 함 
# 각각의 속한 집합의 루트 노드끼리 연결하는 것이 union 즉, x, y를 연결하기보다 x,y의 부모가 되는 녀석을 연결 
def union(parent, x, y) :
    parent_x = find_parent(parent, x)
    parent_y = find_parent(parent, y)

    # 부모를 기록할 때는 값이 더 작은 노드를 선택한다.(그냥 그렇게 함)
    # 특정 노드의 부모를 찾아온 부모로 설정하는 것 
    if parent_x < parent_y :
        parent[parent_y] = parent_x
    else :
        parent[parent_x] = parent_y

def union_find() :

    node_count, edge_count = map(int, sys.stdin.readline().split())
    
    parent_table = [i for i in range(node_count + 1)]

    for _ in range(edge_count) :
        a, b = map(int, sys.stdin.readline().split())

        # 서로 동일한 집합에 속하지 않는다면 하나의 집합으로 묶어 준다. 
        if find_parent(parent_table, a) != find_parent(parent_table, b) :
            union(parent_table, a, b)
        else :
            print("이미 동일한 집합인뎅 ?")

    for curr_index in range(1, node_count + 1) :
        print(find_parent(parent_table, curr_index), end = " ")
union_find()