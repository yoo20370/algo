import sys
from collections import deque

INF = int(1e9)

v, e = map(int, sys.stdin.readline().split())

graph = [[] for i in range(v+1)]

entryOrder = [0] * (v+1) 

entryOrder[0] = INF
for i in range(e) :
    start, end = map(int, sys.stdin.readline().split())
    # 그래프에 데이터 삽입
    graph[start].append(end)

    # 진입차수 설정 
    entryOrder[end] += 1

def topology_sort() :
    result = []
    queue = deque()

    for i in range(1, len(entryOrder)) :
        if entryOrder[i] == 0 :
            queue.append(i)
    
    while queue :

        startNode = queue.popleft()
        result.append(startNode) 

        for currNode in graph[startNode] :
            entryOrder[currNode] -=1
            if entryOrder[currNode] == 0 :
                queue.append(currNode)
    
    return result

for i in topology_sort() :
    print(i, end=" ")






    
