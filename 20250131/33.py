import sys 
from collections import deque 

v, e = map(int, sys.stdin.readline().split())

entry_cnt = [0] * (v + 1)

graph = [[] for _ in range(v+1)]

for _ in range(e) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    entry_cnt[b] += 1

queue = deque()

for i in range(1, v+1) :
    # 진입 차수 0인 경우 
    if entry_cnt[i] == 0 :
        queue.append(i)

while queue :
    curr_node = queue.popleft()
    print(curr_node, end=" ")

    for near_node in graph[curr_node] :
        # 연결 끊기 
        entry_cnt[near_node] -= 1
        if entry_cnt[near_node] == 0 :
            queue.append(near_node)

