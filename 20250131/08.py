
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

def dfs(node, graph, visited) :

    visited[node] = True
    print(node, end=" ")

    for curr_node in graph[node] :
        if not visited[curr_node] :
            dfs(curr_node, graph, visited)

dfs(1, graph, visited)

def dfs_stack_simulate(start, graph):
    visited = [False] * len(graph)
    # (노드, 몇 번째 인접 노드를 확인 중인지)
    stack = [(start, 0)]
    
    visited[start] = True
    print(start, end=" ")

    while stack:
        curr_node, idx = stack.pop()
        
        # 아직 curr_node의 인접 노드를 다 확인 못 했다면,
        if idx < len(graph[curr_node]):
            # 지금 인덱스를 1 증가시켜 "다음 인접 노드"도 확인하도록
            stack.append((curr_node, idx + 1))

            next_node = graph[curr_node][idx]
            if not visited[next_node]:
                visited[next_node] = True
                print(next_node, end=" ")
                # next_node에 대해서도 인접 리스트를 처음(0번 인덱스)부터 볼 것
                stack.append((next_node, 0))
        # 만약 curr_node의 모든 인접 노드를 다 확인했다면, 그냥 pop하고 끝
        # (즉, 재귀에서 'return'하는 것과 동일)
    
    print()  # 줄바꿈

dfs_stack_simulate(1, graph)