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

def bfs(graph, start) -> None :

    # 시작 노드를 스택에 넣는다. 
    # 스택이 빌 때까지 반복문을 수행한다.
    # 스택에서 값을 꺼내서 방문처리한다.
    # 꺼낸 값에 대하여 인접한 노드들을 순회하며 방문하지 않았다면 스택에 넣는다.
    # 이 과정을 스택이 빌 때까지 반복한다.

    visited = []
    stack = []
    stack.append(start)

    while stack :
        curr_node = stack.pop()
        visited.append(curr_node)

        for adja_node in sorted(graph[curr_node], reverse=True) :
            if adja_node not in visited :
                stack.append(adja_node)

    return visited
print(bfs(graph, 1))