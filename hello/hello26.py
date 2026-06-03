import sys 


# 합집합 
def union(parent, first, second) :
    
    # 둘 중 더 작은 값에 대하여 부모를 변경하도록 해야함 
    # 여기서 중요한 건 두 원소가 가리키는 각각의 부모 원소 크기를 비교해야 함 
    # 왜냐하면 7번이 2번과 집합을 이루고 8번이 1번과 집합을 이룰 때 7번과 8번을 합집합한다면 -> 1번이 부모가 되는게 맞으니까 
    firstParent = find(parent, first)
    secondParent = find(parent, second)

    if firstParent < secondParent :
        parent[secondParent] = firstParent
    else :
        parent[firstParent] =  secondParent

    # 더 작은 원소를 가리키도록 하면 됨 
    

# 부모를 찾는 것 -> 그냥 부모를 찾는게 아니고 가장 값이 작은 원소를 찾아야 함 
def find(parent, x) :
    # 집합의 부모가 내가 아니라면 -> 다른 집합에 속해 있다면 
    if parent[x] != x :
        # 일단 내가 다른 집합에 속했다면 내가 가리키는 원소의 부모를 찾아야 함 ->
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def solution() :

    n = int(sys.stdin.readline().rstrip())

    # 0은 무시 
    parent = [i for i in range(n + 1)]

    parent1 = find(parent, 1)
    parent2 = find(parent, 2)

    # 서로 같은 집합이 아니라면 ?? 
    if parent1 != parent2 :
        union(parent, 1 ,2)
    
    # 0 1 1 3 4 5 .. n
    print(parent)

solution()