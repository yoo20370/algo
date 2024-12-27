import sys
from collections import deque

def acm_Craft() -> int :
    N, K = map(int, sys.stdin.readline().split())

    entry_cnt = [0] * (N + 1)

    graph = [ [] for i in range(N+1) ]

    cost = [0]

    cost.extend(list(map(int, sys.stdin.readline().split())))

    result = [0] * (N + 1)

    for _ in range(K) :
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        entry_cnt[end] += 1

    final = int(sys.stdin.readline().rstrip())

    queue = deque()

    for i in range(1, N + 1) :
        if entry_cnt[i] == 0 :
            queue.append(i)
            result[i] += cost[i]

    while queue :
        curr_build = queue.popleft()
        
        for curr in graph[curr_build] :
            entry_cnt[curr] -= 1

            result[curr] = max(result[curr], result[curr_build] + cost[curr])
            if entry_cnt[curr] == 0 :
                queue.append(curr)

    print(result[final])

T = int(sys.stdin.readline().rstrip())

result = list()
for _ in range(T) :
    acm_Craft()
