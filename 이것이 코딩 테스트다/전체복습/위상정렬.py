import sys
from collections import deque

def topo_sort(graph, node, edge, entryCnt) -> None :

    queue = deque()

    for idx in range(1, node+1) :
        if entryCnt[idx] == 0 :
            queue.append(idx)
        
    while queue :
        currNode = queue.popleft()
        print(currNode, end=" ")

        for node in graph[currNode] :
            entryCnt[node] -= 1
            if entryCnt[node] == 0 :
                queue.append(node)

node, edge = map(int, sys.stdin.readline().split())

entryCnt = [0] * (node + 1)

graph = [[] for _ in range(node + 1)]

for _ in range(edge) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    entryCnt[end] += 1

topo_sort(graph, node, edge, entryCnt) 

