import sys, heapq

INF = int(1e9)

N = int(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(N+1)]

distance = [INF] * (N+1)

for _ in range(M) :
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append([end, cost])

start, end = map(int, sys.stdin.readline().split())

heap = list()

heapq.heappush(heap, [0, start])
distance[start] = 0

while heap :
    cost, curr = heapq.heappop(heap)

    if distance[curr] < cost :
        continue 
        
    for e, end_cost in graph[curr] :
        temp = cost + end_cost
        if distance[e] > temp :
            distance[e] = temp 
            heapq.heappush(heap, [temp, e])

print(distance[end])