# dfs 
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 스택을 이용해서 풀기 
def solution(graph) :

    stack = []
    visited = []

    stack.append(1)

    while stack :
        currentNode = stack.pop()

        # 이미 방문했다면 방문 할 필요가 없음 
        if currentNode in visited :
            continue 
        
        # 여기서 방문처리 하는 이유 -> 스택에서 꺼낸 순서가 곧 방문 순서이기 때문 
        if currentNode not in visited :
            visited.append(currentNode)

        # 왜 내림차순 ? -> 작은 수 방문해야 하므로 스택 특성상 큰 숫자가 먼저 들어가야 큰 수를 나중에 방문하게 됨 
        for adjacentNode in sorted(graph[currentNode], reverse=True) :
            if adjacentNode not in visited :
                stack.append(adjacentNode)
    
    print(visited)


solution(graph)


# 재귀 함수를 이용해서 풀기
def dfs(graph, currentNode, visited) :

    # 종료 조건
    if currentNode in visited :
        return 
    
    # 방문한 적이 없으니까 방문 처리 
    visited.append(currentNode)

    # 얘는 왜 역순 아님 -> 재귀에서 바로 접근할 것이기 때문에 문제 없음 
    for adjacentNode in graph[currentNode] :

        # 문제 축소 조건 -> 방문처리하는 노드가 많아지게 될 것이고 결국 모두 방문하게 될 것임
        if adjacentNode not in visited :
            dfs(graph, adjacentNode, visited)


visited = []
dfs(graph, 1, visited)

print(visited)
