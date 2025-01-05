import sys
from collections import deque

# 1 익음, 0 익지 않음, -1 토마토 없음 
def tomato(farm_map, row, col, height) :
    temp = 0
    for a in range(height) :
        for b in range(row) :
            for c in range(col) :
                if farm_map[a][b][c] == - 1 or farm_map[a][b][c] == 1:
                    temp += 1
    
    # 이미 모두 익은 경우 
    if temp == (row * col * height) :
        return 0 

    # 상, 하, 동, 서, 남, 북
    distance = [(-1, 0, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]

    # 익을 때까지 걸리는 시간 
    days = 0
    
col, row, height = map(int, sys.stdin.readline().split())

farm_map = [[] for _ in range(height)]

for h in range(height) :
    for r in range(row) :
        farm_map[h].append(list(map(int, sys.stdin.readline().split())))


print(tomato(farm_map, row, col, height))