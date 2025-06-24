# 경쟁적 전염
# N * N 시험관이 존재
# 특정한 위치에 바이러스가 존재할 수 있다.
# 모든 바이러스는 1번 ~ K번까지의 바이러스 종류 중 하나 
# 모든 바이러스는 상하좌우의 방향으로 증식해 나간다. 

## 단 매초마다 번호가 낮은 종류의 바이러스 먼저 증식한다. 
## 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면 그곳에는 다른 바이러스가 들어갈 수 없다. 

## S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성, 만약 S초가 지난 후, 해당 위치에 바이러스가 존재하지 않는다면 0을 출력 
## X, Y는 각각 행과 열의 위치를 의미 
## 가장 좌측 위쪽은 1, 1

import sys, heapq
from collections import deque 

def solution() :

    N, virus_kind  = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    target_time, x, y = map(int, sys.stdin.readline().split())

    distance = [(0,1), (0,-1), (1,0), (-1,0)]

    queue = []
    for r in range(N) :
        for c in range(N) :
            if graph[r][c] != 0 :
                queue.append((graph[r][c], r,c))

    # 정렬을 수행하여, 숫자가 작은 바이러스 부터 뽑히도록 함 -> 나중에도 작은 바이러스부터 들어가므로 작은 바이러스 만큼 들어가게 됨 
    queue.sort(key=lambda x : x[0])
    queue = deque(queue)

    time = 0
    while time < target_time :
        time += 1

        # 해당 time 동안에 들어온 좌표에 대해서만 확장 시도 
        for _ in range(len(queue)) :
            curr_virus, curr_row, curr_col = queue.popleft()

            for next_row, next_col in distance :
                move_row = curr_row + next_row
                move_col = curr_col + next_col 

                # 범위 내에 존재하고 방문한 적이 없다면 
                if move_row >= 0 and move_row < N and move_col >= 0 and move_col < N and graph[move_row][move_col] == 0 :
                    graph[move_row][move_col] = curr_virus
                    queue.append((graph[move_row][move_col], move_row, move_col))
        
    return graph[x-1][y-1]

print(solution())