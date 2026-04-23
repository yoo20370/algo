import sys

sys.setrecursionlimit(int(1e5))

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
visited = []

## 깊이 우선 탐색 -> 가장 깊은 곳 부터 탐색하는 방식 
## 재귀로 구현하는 경우 
## 방문한 노드는 방문 처리 한다.
## 현재 노드의 인접 리스트를 순회하면서, 방문하지 않았다면 다시 DFS 재귀를 돌도록 한다.
## 재귀이기 때문에 종료 조건은 무엇인가 ??
## 축소 조건은 무엇인가 ?? 
## 내가 생각하면서 풀어야 함 

def dfs_recursion(adjacent_graph, cur_node, visited_array):

    # 문제 축소 -> 왜냐하면, 방문처리함으로써 방문할 노드의 개수를 줄이고 있음 
    visited_array.append(cur_node)

    for node in adjacent_graph[cur_node] :
        if node not in visited_array :
            dfs_recursion(adjacent_graph, node, visited_array)

    return

dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!