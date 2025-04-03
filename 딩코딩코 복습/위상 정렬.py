from collections import deque
import sys

# 진입차수가 적은 것부터 순서대로 접근해야 한다.
# 간선이 들어오면서 진입 차수를 센다.모두 저장 후, 진입차수 테이블을 순회하여 진입차수가 0인 것을 큐에 삽입한다.
# 큐에서 값을 꺼내서 결과 리스트에 넣고 인접한 노드들의 진입차수를 1씩 깍고, 진입차수가 0이면 큐에 삽입한다.
# 이 과정을 큐가 빌 떄까지 반복한다.
# O(V + E) -> 큐에 V가 한 번씩 들어갔다 나오며 나온 노드와 인접한 노드에 대하여 검증을 수행하기 때문
node_cnt, edge_cnt = map(int, sys.stdin.readline().split())

entry_table = [0 for i in range(node_cnt + 1)]
graph = [[] for i in range(node_cnt + 1)]
for _ in range(edge_cnt) :
    start, end = map(int, sys.stdin.readline().split())

    graph[start].append(end)
    entry_table[end] += 1


def topo_sort(entry_table, graph) :

    result = []

    queue = deque()
    for index in range(1, len(entry_table)) :
        if entry_table[index] == 0 :
            queue.append(index)

    while queue : 
        curr_node = queue.popleft()
        result.append(curr_node)

        for node in graph[curr_node] : 
            entry_table[node] -= 1
            if entry_table[node] == 0 :
                queue.append(node)

    return result

for node in topo_sort(entry_table, graph) :
    print(node, end=" ")
