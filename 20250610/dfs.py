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

def dfs(start) :
    # 시작 노드를 스택에 넣는다.
    # 스택이 비어있지 않다면, 스택에서 값을 하나 뽑고 방문처리 해준 다음 해당 스택과 연결된 노드를 방문한다.
    # 이 과정을 모든 노드를 방문할 때까지 반복한다. 

    visited = []
    stack = [start]

    while stack :
        curr_node = stack.pop()
        visited.append(curr_node)

        for near_node in sorted(graph[curr_node], reverse=True) :
            if near_node not in visited :
                stack.append(near_node)

    return visited

for i in dfs(1) :
    print(i, end=" ")