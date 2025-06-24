# 벽은 3개를 세울 수 있다.
# 0이 아닌 곳 3개를 임의로 설치한다. 
# 바이러스를 BFS로 전파한다.
# 0인 곳을 count한다.

# 2차원 배열을 모두 순회해서, 0인 좌표, 2인 좌표를 모두 구한다.

# permutations을 이용해서 벽을 세울 위치 3개를 조합으로 만든다.
# 2인 위치에 대하여 bfs를 수행하고, 방문한 위치를 2로 설정한다.
# 2차원 배열을 순회하여 값이 아직 0인 위치를 계산한다.

import sys, copy
from itertools import permutations
from collections import deque

def solution() :

    row, col = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(row) :
        graph.append(list(map(int, sys.stdin.readline().split())))


    build_wall_list = []
    virus_list = []

    for r in range(row) :
        for c in range(col) :
            if graph[r][c] == 0 :
                build_wall_list.append((r,c))
            elif graph[r][c] == 2 :
                virus_list.append((r,c))

    distance = [(0, 1), (0, -1), (1, 0), (-1,0)]

    max_count = 0
    # 무조건 3개를 만들어야 함 
    for build_wall in permutations(build_wall_list, 3) :
        print(build_wall)
        
        new_graph = copy.deepcopy(graph)

        for curr_row, curr_col in build_wall :
            new_graph[curr_row][curr_col] = 1

        queue = deque()
        for r, c in virus_list :
            queue.append((r,c))

        while queue :
            curr_row, curr_col = queue.popleft()

            # 사방면 확인 
            for move_row, move_col in distance :
                
                next_row = curr_row + move_row
                next_col = curr_col + move_col

                # 그래프 내에 존재하고, 전파 가능한 빈 공간인 경우 
                if next_row >= 0 and next_row < row and next_col >= 0 and next_col < col and new_graph[next_row][next_col] == 0 :
                    new_graph[next_row][next_col] = 2 
                    queue.append((next_row, next_col))                                        

        count = 0
        for r in range(row) :
            for c in range(col) :
                if new_graph[r][c] == 0 :
                    count += 1

        max_count = max(max_count, count)

    return max_count
        

print(solution())