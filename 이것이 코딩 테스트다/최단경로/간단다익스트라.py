import sys 

INF = int(10e9)

N, M = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(N+1)]


for i in range(M) :
    node, end, val = map(int, sys.stdin.readline().split())
    graph[node].append([end, val])

minDis = [INF] * (N+1)
visited = [False] * (N+1)

# 최단 거리 리스트를 순회하여 가장 작은 값을 반환하는 함수 
def getSmallNode(minDis, visited, start) :
    minIdx = 0
    for idx in range(1,len(minDis)) :
        if idx == start or visited[idx] == True:
            continue
        # 최단 거리 값이 가장 작은 idx를 찾는 조건문 
        if minDis[minIdx] > minDis[idx] :
            minIdx = idx

    return idx

def dijkstra(start) :
    
    minDis[start] = 0
    curr = start
    visited[start] = True
    
    for _ in range( N - 1 ):
        for node in graph[curr] :
            end, val = node
            minDis[end] = min(minDis[end], minDis[curr] + val)
            
        # 최단 거리 리스트에서 값이 가장 작은 노드를 선택
        next = getSmallNode(minDis, visited, start) 
        if next == 0 :
            break
        # 다음 노드를 현재 노드로 변경 
        visited[next] = True
        curr = next 

dijkstra(start) 

for i in minDis :
    if minDis != INF :
        print(minDis)
    else :
        print("INF")
        
