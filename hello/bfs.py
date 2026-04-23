from collections import deque

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 어떻게 풀어야 하지 ??
# 방문하면 visited에 삽입 (set) 
# 해당 노드의 인접 리스틀르 순회하면서 방문하지 않았다면, 큐에 삽입한다. 
# 큐에서 값을 꺼내어 동일한 작업 수행 

def bfs_queue(adj_graph, start_node):

    visited = set([start_node])
    result = []
    queue = deque([start_node])

    while queue :
        currentNode = queue.popleft()
        result.append(currentNode)

        for adjNode in adj_graph[currentNode] :
            if adjNode not in visited :
                queue.append(adjNode)
                visited.add(adjNode)
    
    return result

print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!