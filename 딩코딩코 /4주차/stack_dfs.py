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


# def dfs_stack(adjacent_graph, start_node):
#      # 방문하지 않은 노드의 경우 방문처리를 한다.
#     # 스택의 맨 위 노드를 기준으로 graph를 순회한다. 
#     # 만약 모든 노드를 순회했다면 stack에서 pop한다. 

#     visited = [False] * (len(graph) + 1)

#     stack = [start_node]
#     visited[start_node] = True
#     result = [start_node]
    
#     while stack :
#         curr_node = stack[-1]
#         visit_count = 0 

        
#         for visit_node in sorted(graph[curr_node], reverse=True) :
#             if not visited[visit_node] :
#                 visited[visit_node] = True
#                 result.append(visit_node)
#                 stack.append(visit_node)
#                 break
#             visit_count += 1
        
#         if visit_count == len(graph[curr_node]) :
#             stack.pop()
#     return result

def dfs_stack(adjacent_graph, start_node):

    result = []

    visited = [False] * (len(graph) + 1)
    stack = [start_node]

    while stack :
        curr_node = stack.pop()

        if not visited[curr_node] :
            visited[curr_node] = True
            result.append(curr_node)

            for visit_node in sorted(adjacent_graph[curr_node], reverse=True) :
                if not visited[visit_node] :
                    stack.append(visit_node)
        
    return result


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!