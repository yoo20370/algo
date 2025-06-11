from collections import deque

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

def bfs(start) :
    # 큐에 시작 노드를 삽입한다.
    # 큐에 값이 존재한다면, 큐에서 값을 꺼내고 방문처리한다.
    # 큐와 인접한 노드를 차례대로 큐에 삽입한다.
    # 위 과정을 큐가 빌 때까지 수행한다.
    visited = []
    queue = deque()
    queue.append(start)

    while queue :
        curr_node = queue.popleft()
        visited.append(curr_node)

        for near_node in graph[curr_node] :
            if near_node not in visited :
                queue.append(near_node)

    return visited

for i in bfs(1) :
    print(i, end=" ")
