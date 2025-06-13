import sys
from collections import deque

# 위상 정렬이란 모든 정점에 대해서 선행되어야 할 순서를 고려해 나열하는 정렬 알고리즘 
# 구현 어떻게 할까 ?? 
# 진입 차수를 카운트하여 진입 차수 테이블에 저장한다.
# 진입 차수 테이블을 순회하여 진입 차수가 0인 모든 노드를 큐에 삽입한다.
# 큐에서 노드를 꺼내고 인접한 노드의 진입차수를 1씩 빼고, 여기서 진입차수가 0인 것을 다시 큐에 삽입한다.   
# 이 과정을 모든 노드에 접근할 떄까지 수행한다. 

def topological_sort() :
    node_count, edge_count = map(int, sys.stdin.readline().split())

    entry_table = [0] * (node_count + 1)
    graph = [[] * (node_count + 1) for _ in range(node_count + 1)]
    for _ in range(edge_count) :
        start, end = map(int, sys.stdin.readline().split())
        # 큐에서 꺼냈을 때, 간선을 제거해야할 인접 노드 리스트 
        graph[start].append(end)

        # 진입 차수 기록 테이블
        entry_table[end] += 1

    
    queue = deque()


    for node_number in range(1, len(entry_table)) :
        if entry_table[node_number] == 0 :
            queue.append(node_number)

    result = []    
    while queue :
        curr_node = queue.popleft()
        result.append(curr_node)

        for near_node in graph[curr_node] :
            entry_table[near_node] -= 1

            if entry_table[near_node] == 0 :
                queue.append(near_node)

    return result

print(topological_sort())



