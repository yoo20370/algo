import sys, copy
from collections import deque
N = int(sys.stdin.readline().rstrip())

# 진입 차수
entry_count = [0] * (N+1)

graph = [ [] for i in range(N+1)]

cost = [0] * (N+1)

for i in range(1, N+1) :
    data = list(map(int, sys.stdin.readline().split()))
    # 비용 추가 
    cost[i] = data[0]

    # 연결 관계 설정 및 진입 차수 계산 
    for end in data[1:-1] :
        graph[end].append(i)
        entry_count[i] += 1

result_cost = copy.deepcopy(cost)

queue = deque()

for i in range(1, N+1) :
    if entry_count[i] == 0 :
        queue.append(i)

while queue :
    curr_node = queue.popleft() 

    for near_node in graph[curr_node] :
        # 연결 끊기
        result_cost[near_node] = max(result_cost[near_node], result_cost[curr_node] + cost[near_node])
        entry_count[near_node] -= 1
        if entry_count[near_node] == 0 :
            queue.append(near_node)

for i in result_cost :
    print(i)