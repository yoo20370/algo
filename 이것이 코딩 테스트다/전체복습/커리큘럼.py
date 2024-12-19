import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(N+1)]

entryCnt = [0] *(N+1)

cost = [0] * (N+1)

for idx in range(1,N+1) :
    data = list(map(int, sys.stdin.readline().split()))
    cost[idx] = data[0]
    for j in range(1,len(data) -1) :
        graph[data[j]].append(idx)

    entryCnt[idx] = len(data) - 2

result = [0] * (N + 1)

queue = deque()

for i in range(1, N+1) :
    if entryCnt[i] == 0 :
        queue.append(i)
        result[i] = cost[i]


while queue : 
    currNode = queue.popleft()

    for node in graph[currNode] :
        entryCnt[node] -= 1
        
        result[node] = max(result[node], result[currNode] + cost[node])
        if entryCnt[node] == 0 :
            queue.append(node)

for i in range(1, N+1) :
    print(result[i])