# 시간 복잡도 O(V^2)
# 노드의 개수 5,000개 이하라면 이 코드를 사용해서 문제를 풀 수 있다. 
# 노드의 개수가 10,000개를 넘어가는 문제라면 이 코드로는 문제를 해결하기 어렵다.
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

    return minIdx

def dijkstra(start) :
    
    # 시작점 0으로 표시
    minDis[start] = 0
    curr = start
    visited[start] = True
    
    # 노드 수 만큼 방문하기 위해서 N - 1번 실행 
    for _ in range( N - 1 ): 
        for node in graph[curr] :
            end, val = node
            minDis[end] = min(minDis[end], minDis[curr] + val)
            
        # 최단 거리 리스트에서 값이 가장 작은 노드를 선택
        next = getSmallNode(minDis, visited, start) 
        # 다음 노드를 현재 노드로 변경 
        visited[next] = True
        curr = next 

dijkstra(start) 

for i in range(1,len(minDis)) :
    if minDis[i] != INF :
        print(minDis[i])
    else :
        print("INF")
        
