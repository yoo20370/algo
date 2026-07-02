# 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하고자 한다. 
# 이때 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추려고 함 

# 송전탑의 개수 n, 전선 정보 wires가 매개변수로 주어졌을 때, 전선들 중 하나를 끊어서 
# 송전탑의 개수가 가능한 비슷하도록 두 전력망을 나누었을 때
# 두 전력망이 가지고 있는 송전탑 개수의 차이를 return하도록 해달라 

# 생각을 해보자 
# 두 가지 방법이 떠오름
# dfs와 union-find 

# dfs 같은 경우는 일단 임의의 간선을 제거하고 
# 두 점을 기준으로 dfs를 탐색을 통해 각각 몇 개의 노드를 방문했는지 확인
# | A - B |를 통해서 값을 계산한다. abs() 메서드 활용 

INF = int(1e9)

def dfs(startNode, visited, wires) :
    
    stack = []
    
    stack.append(startNode)
    
    while stack :
        currentNode = stack.pop()
        
        if currentNode in visited:
            continue
            
        visited.add(currentNode)
        
        for wire in wires :
            start, end = wire 
            
            if start == currentNode and end not in visited :
                stack.append(end)
            
            if end == currentNode and start not in visited : 
                stack.append(start)
    
    return len(visited) - 1
            
    
def solution(n, wires):
    
    minCount = INF
    for cutWire in wires :
        a, b = cutWire
        
        resultA = dfs(a, set([b]), wires)
        
        resultB = dfs(b, set([a]), wires)
        
        minCount = min(minCount, abs(resultA - resultB))
        
    return minCount