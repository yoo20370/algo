import heapq

import sys 

INF = int(1e9)

node_cnt, edge_cnt = map(int, sys.stdin.readline().split())

start_node = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(node_cnt + 1)]

for _ in range(edge_cnt) :
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])


# 시작 노드를 힙에 넣는다.
# 시작 노드의 최단 거리를 0으로 설정한다.
# 힙에서 최단 거리인 노드를 꺼낸다.
# 꺼낸 노드의 비용이 최단 거리 리스트의 비용보다 크다면 이미 방문한 것이므로 돌아간다.
# 그렇지 않으면 인접한 노드들에 대하여 최단 거리를 계산한다.
# 최단 거리 리스트의 비용보다 작다면 힙에 최단 거리 리스트를 갱신하고 힙에 삽입한다. 
# 모든 노드를 순회할 때까지 이를 반복한다.

def dijkstra(start_node, node_cnt) -> None :

    distance = [INF] * (node_cnt + 1)
    heap = []
    heapq.heappush(heap, [0, start_node])
    distance[start_node] = 0

    while heap :
        curr_cost, curr_node = heapq.heappop(heap)

        if distance[curr_node] < curr_cost :
            continue

        for end_node, end_cost in graph[curr_node] :
            temp_cost = curr_cost + end_cost
            if distance[end_node] > temp_cost :
                distance[end_node] = temp_cost
                heapq.heappush(heap, [temp_cost, end_node])
    

    for index in range(1, len(distance)) :
        print(distance[index])


dijkstra(start_node, node_cnt)
