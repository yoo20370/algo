from collections import deque
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

def dfs(graph, start) -> None :
    # 시작 노드를 큐에 삽입한다.
    # 큐에서 노드를 꺼낸다.
    # 꺼낸 노드를 방문처리 한다. 
    # 노드에 인접한 노드들을 순회하면서 방문처리 하지 않았다면 큐에 삽입한다.
    # 큐가 빌때까지 이를 반복한다. 

    visited = []
    queue = deque()
    queue.append(start)

    while queue:
        curr_node = queue.popleft()
        visited.append(curr_node)

        for adja_node in graph[curr_node] :
            if adja_node not in visited :
                queue.append(adja_node)
    
    return visited

print(dfs(graph, 1))