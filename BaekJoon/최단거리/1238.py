import sys, heapq

# 목적지에서 집으로 구할 때 사용 
def dijkstra(start, time_slice) -> None :

    time_slice[start] = 0 
    heap = list()

    heapq.heappush(heap, [0, start])

    while heap :
        curr_time, s = heapq.heappop(heap)

        if time_slice[s] < curr_time :
            continue

        for e, time in graph[s] :
            times = curr_time + time
            if time_slice[e] > times :
                time_slice[e] = times
                heapq.heappush(heap, [times, e])

INF = int(1e9)

N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M) :
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append([end, time])

time_slice1 = [[INF] *(N+1) for i in range(N+1)]
time_slice2 = [INF] * (N+1)

result = [0] * (N+1)
# 시작 값 구하기
for i in range(1, N+1) :
    dijkstra(i, time_slice1[i])
    
    dijkstra(X, time_slice2)

    result[i] = time_slice1[i][X] + time_slice2[i]

print(max(result))



