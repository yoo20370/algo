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

def dfs(graph, start_node) -> None :


    # 방문하지 않은 노드의 경우 방문처리를 한다.
    # 스택의 맨 위 노드를 기준으로 graph를 순회한다. 
    # 만약 모든 노드를 순회했다면 stack에서 pop한다. 

    visited = [False] * (len(graph) + 1)

    stack = [start_node]
    visited[start_node] = True
    print(start_node, end=" ")
    
    while stack :
        curr_node = stack[-1]
        visit_count = 0 

        for visit_node in graph[curr_node] :
            if not visited[visit_node] :
                visited[visit_node] = True
                print(visit_node, end=" ")
                stack.append(visit_node)
                break
            visit_count += 1
        
        if visit_count == len(graph[curr_node]) :
            stack.pop()

def dfs2(graph, start_node):
    stack = [start_node]
    visited = [False] * (len(graph) + 1)

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            # 스택을 사용하므로, 오름차순으로 탐색하려면 역순으로 삽입해야 함
            for neighbor in sorted(graph[node], reverse=True):
                if not visited[neighbor]:
                    stack.append(neighbor)


dfs2(graph, 1)