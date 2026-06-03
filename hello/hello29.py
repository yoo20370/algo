import sys
from collections import deque
# 위상 정렬

def solution() :
    nodeCount, edgeCount = map(int, sys.stdin.readline().split())

    # 진입 차수
    entryDegree = [0] * (nodeCount + 1)

    graph = [[] for _ in range(nodeCount + 1)]

    for _ in range(edgeCount) :
        start, end = map(int, sys.stdin.readline().split())

        # 어디서 어디로 가는지 기록 
        graph[start].append(end)

        # 진입차수 증가 
        entryDegree[end] += 1

    # 진입차수가 0이면 들어가야 함 
    queue = deque()

    for index in range(1, nodeCount + 1) :
        if entryDegree[index] == 0 :
            queue.append(index)

    visited = []


    while queue :
        currentNode = queue.popleft()
        
        # 큐에서 꺼낸다는 건 방문한다는 것 
        visited.append(currentNode)

        # 인접한 노드를 순회하는 것 
        for adjacentNode in graph[currentNode] :
            
            # 연관된 노드 진입 차수 제거
            entryDegree[adjacentNode] -= 1

            # 연결된 노드 중 진입차수가 0이 되면 큐에 삽입한다. 
            if entryDegree[adjacentNode] == 0 :
                queue.append(adjacentNode)
    
    if len(visited) != nodeCount :
        print("사이클 존재")

    print(visited)

solution()