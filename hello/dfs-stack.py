# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 생각을 해봅시다.
# 스택에 넣는다. -> 스택에서 꺼낸 뒤, 방문처리하고, 인접한 노드들을 스택에 넣는다.
# 스택에서 꺼내어 반복한다. 

def dfs_stack(adjacent_graph, start_node):

    visitied = set([start_node])
    result = []
    stack = [start_node]

    while stack :
        currentNode = stack.pop()
        result.append(currentNode)

        for node in adjacent_graph[currentNode] : 
            if node not in visitied :
                stack.append(node)
                visitied.add(node)

    return result

print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!