# dfs나 bfs를 통해서 인접한 노드를 탐색하는 방식으로 풀 수 있고
# union find로도 풀 수 있다. 
# union-find로 풀게 되면 행렬을 하나하나 순회하면서, union 하면 될 것 같음 
# 그리고 모든 노드에 대해서 find를 한 번 돌린 후 부모가 서로 다른 게 몇 개인지 확인하면 될 것 같음 

# dfs나 bfs로 풀게 되는 경우 
# 행렬을 순회하면서, 인접한 노드를 탐색하게 하는 것 
# 이때, 한 번 bfs나 dfs를 수행할 때 count를 증가시킨다.

# 두 가지 방식으로 모두 풀어보자 

# union-find 방식으로 풀기 
def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y) :
    parentX = find(parent, x)
    parentY = find(parent, y)
    
    if parentX < parentY :
        parent[parentY] = parentX
    else :
        parent[parentX] = parentY

def solution(n, computers):
    
    parent = [i for i in range(n)]
    
    for row in range(len(computers)) :
        for col in range(len(computers[row])) :
            if row != col and computers[row][col] == 1 :
                if find(parent, row) != find(parent, col) :
                    union(parent, row, col)
    
    for x in range(0, n ) :
        find(parent, x)

    print(parent)
    
    parentSet = set()
    for x in range(0, n) :
        parentSet.add(parent[x])
    
    answer = len(parentSet)
    return answer

# dfs로 풀어보자 

def dfs(n, computers, firstNode, secondNode) :

    stack = []
    
    stack.append((firstNode, secondNode))
    
    while stack :
        leftNode, rightNode = stack.pop()
        
        if computers[leftNode][rightNode] != 1 : 
            continue
        
        computers[leftNode][rightNode] = 2
        computers[rightNode][leftNode] = 2
        
        for adjacentNode in range(n) :
            if computers[rightNode][adjacentNode] == 1 :
                stack.append((rightNode, adjacentNode))
        
        
def solution(n, computers):
    
    count = 0 
    for row in range(n) :
        for col in range(n) :
            if computers[row][col] == 1 :
                dfs(n, computers, row, col)
                count += 1
    
    return count