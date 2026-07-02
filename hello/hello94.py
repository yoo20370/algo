# 첫 번째 풀이는 주어진 wires를 가지고 푸는 것이 목적이었음
# 다만 매번 wires를 순회해야한다는 점 때문에 시간복잡도가 비효율적이었음 

# 그래서 이를 개선하고자 함 
# 그래서 wires를 graph로 변환한 후, 처리하고자 함 

INF = int(1e9)

def dfs(startNode, visited, graph) :
    
    stack = [startNode]
    
    while stack :
        currentNode = stack.pop()
        
        if currentNode in visited :
            continue
        
        visited.add(currentNode)
        
        for adjacentNode in graph[currentNode] :
            if adjacentNode not in visited :
                stack.append(adjacentNode)
                
    return len(visited) - 1

def solution(n, wires):
    
    graph = {}
    for index in range(len(wires)) :

        start, end = wires[index]

        if graph.get(start) is None :
            graph[start] = [end]
        else :
            graph[start].append(end)

        if graph.get(end) is None :
            graph[end] = [start]
        else :
            graph[end].append(start)
    
    minCount = INF
    for currentIndex in range(len(wires)) :
        a, b = wires[currentIndex]
        
        resultA = dfs(a, set([b]), graph)
        resultB = dfs(b, set([a]), graph)
        
        
        minCount = min(minCount, abs(resultA - resultB))
        
    return minCount