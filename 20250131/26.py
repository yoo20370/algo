import sys, heapq

INF = int(1e5)

node, edge = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline().rstrip())

distance = [INF] * (node + 1)

edges = [ [] for i in range(node + 1) ]

for _ in range(edge) :
    start_node, end_node, cost = map(int, sys.stdin.readline().split())
    edges[start_node].append([end_node, cost])

# 힙은 “최단 거리 후보”들을 저장하는 역할
heap = list()
distance[start] = 0

# 가장 거리가 짧은 거리의 노드를 먼저 확정하면, 그 거리까지의 계산이 항상 최소값을 유지"
heapq.heappush(heap, (0, start))

while heap :
    # 현재 까지 발견된 노드 중, 가장 작은 것을 반환하므로 힙에서 꺼낼 때, 최단 거리 확정
    curr_cost, curr_node = heapq.heappop(heap)

    # 이미 계산되었다면 heap에 넣을 때보다 테이블의 최단거리 값이 더 작을 것 
    if distance[curr_node] < curr_cost :
        continue 

    for end_node, cost in edges[curr_node] :
        temp_cost = cost + curr_cost 
        if distance[end_node] > temp_cost :
            distance[end_node] = temp_cost
            heapq.heappush(heap, (temp_cost, end_node))

for i in distance :
    print(i)






