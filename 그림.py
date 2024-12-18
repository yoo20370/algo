import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

# pan이 방문처리 
pan = list()

for i in range(N) :
    pan.append(list(map(int, sys.stdin.readline().split())))

# 동, 서, 남, 북 
# direction = [(1,0),(-1,0),(1,0),(-1,0)]
direction = [(0,1),(0,-1),(1,0),(-1,0)]


def bfsIce(start) :
    size = 0
    x, y = start 
    # 시작 위치가 이미 방문한 경우 바로 리턴 
    if pan[x][y] == 0 :
        return 0, 0

    queue = deque()

    # 시작 위치 방문 처리 
    queue.append((x,y))
    pan[x][y] = 0

    while queue :
        currX, currY = queue.popleft()

        # 노드의 동, 서, 남, 북에 대하여 너비 우선 탐색 수행 
        for a, b in direction :
            xx = currX + a
            yy = currY + b
            if  xx > -1 and xx < N and yy > -1 and yy < M and pan[xx][yy] == 1:
                queue.append((xx,yy))
                size += 1
                pan[xx][yy] = 0
    return 1, size

size = 0
cnt = 0 
for i in range(N) :
    for j in range(M) :
        start = (i, j) 
        a, b = bfsIce(start)
        cnt += a 
        size = max(size, b)

print(cnt, size+1)


    