# 그림의 개수와 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하라 
# 그냥 BFS로 돌면서 몇 번의 BFS를 수행했고, BFS 중 가장 많이 탐색한 경우를 처리하면 될 것 같다. 
import sys 
from collections import deque

def isValidPosition(curr_row, curr_col, row, col, graph) : 
    if curr_row >= 0 and curr_row < row and curr_col >= 0 and curr_col < col and graph[curr_row][curr_col] == 1 :
        return True
    return False

def solution() :
    row, col = map(int, sys.stdin.readline().split())

    graph = []
    for _ in range(row) :
        graph.append(list(map(int, sys.stdin.readline().split())))

    picture_count = 0
    max_extend = 0

    direction = [(1,0), (-1,0), (0,1), (0,-1)]

    for r in range(row) :
        for c in range(col) :
            if graph[r][c] == 1 : 
                picture_count += 1 
                picture_extend = 1

                queue = deque()
                queue.append((r,c))
                graph[r][c] = 0

                while queue :
                    curr_row, curr_col = queue.popleft()

                    # 상하좌우 확인 
                    for move_row, move_col in direction :
                        
                        # 이동할 위치
                        next_row = curr_row + move_row
                        next_col = curr_col + move_col

                        # 위치가 타당하다면 
                        if isValidPosition(next_row, next_col, row, col, graph) :
                            queue.append((next_row, next_col))
                            graph[next_row][next_col] = 0 
                            picture_extend += 1 

                max_extend = max(max_extend, picture_extend)  

    if picture_count == 0 :
        print(0)
        print(0)
        return     
    print(picture_count)
    print(max_extend)

solution()