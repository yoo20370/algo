import sys
import heapq

INF = int(1e9)

def dijkstra():

    node_count, edge_count = map(int, sys.stdin.readline().split())
    init_node = int(sys.stdin.readline().rstrip())

    distance = [INF] * (node_count + 1)
    graph = [[] for _ in range(node_count + 1)]

    for _ in range(edge_count) :
        start_node, end_node, cost = map(int, sys.stdin.readline().split())
        graph[start_node].append([cost, end_node])

    distance[init_node] = 0
    priority_queue = []

    heapq.heappush(priority_queue, [0, init_node])

    while priority_queue :
        curr_cost, curr_node = heapq.heappop(priority_queue)

        if distance[curr_node] < curr_cost :
            continue

        for near_cost, near_node in graph[curr_node] :
            min_distance = curr_cost + near_cost
            if distance[near_node] > min_distance :
                distance[near_node] = min_distance
                heapq.heappush(priority_queue, [min_distance, near_node])

    for index in range(1, node_count + 1) :
        print(distance[index])
dijkstra()