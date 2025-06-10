import sys
from collections import deque

v, e = map(int, sys.stdin.readline().split())

entryCnt = [0] * (v+1)

graph = [[] for i in range(v+1)]

for _ in range(e) :
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    entryCnt[end] += 1

def topo_sort() :
    result = []
    queue = deque()

    for i in range(1, v+1) :
        if entryCnt[i] == 0 :
            queue.append(i)
    
    while queue :
        currNode = queue.popleft()
        result.append(currNode)

        for connNode in graph[currNode] :
            entryCnt[connNode] -= 1
            if entryCnt[connNode] == 0 :
                queue.append(connNode)
    return result

result = topo_sort() 

for i in result :
    print(i, end = " ")