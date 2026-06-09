# 위상 정렬 
import sys
from collections import deque

def solution() :
    nodeCount, edgeCount = map(int, sys.stdin.readline().split())

    # 이 그래프에는 특정 노드에서 특정 노드로 간다는 것을 기록할 것 
    graph = [[] for _ in range(nodeCount + 1)]

    entryCountList = [0] * (nodeCount + 1)
    for _ in range(edgeCount) :
        start, end = map(int, sys.stdin.readline().split()) 

        graph[start].append(end)
        entryCountList[end] += 1

    queue = deque()

    # 진입 차수가 0인 경우를 모두 삽입 
    for index in range(1, nodeCount + 1) :
        if entryCountList[index] == 0 :
            queue.append(index)
    
    visited = []

    while queue :
        currentNode = queue.popleft()

        # 방문처리를 할 필요가 있는가 ??
        # 없어도 될 것 같다. 애초에 진입차수가 0이 된 노드들만 queue에 삽입됨
        # 방문처리를 하지 않아도 무한루프를 돌지 않으며, 딱 한 번만 돌게 됨 

        # 큐에서 꺼냈다는 건 실행하겠다는 의미 
        visited.append(currentNode)

        # 인접한 노드를 순회하면서 진입 차수 낮추기 
        for adjarcentNode in graph[currentNode] :
            entryCountList[adjarcentNode] -= 1

            # 진입 차수가 0이라면 이제 수행 가능하므로 큐에 삽입 
            if entryCountList[adjarcentNode] == 0 :
                queue.append(adjarcentNode)

    if len(visited) != nodeCount :
        print("사이클이 존재합니다.")
        return -1

    return visited

solution()