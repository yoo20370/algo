import sys 
from collections import deque


N, M = map(int, sys.stdin.readline().split())

pan = list()
for i in range(N) :
    pan.append(list(map(int, sys.stdin.readline().rstrip())))


direction = [(0,1), (0,-1),(1,0),(-1,0)]

def miroEscape(start, end) :
    queue = deque()
    queue.append((start,end))

    while queue :
        currX, currY = queue.popleft()

        if currX == N -1 and currY == M -1 :
            return pan[currX][currY]
        
        currVal = pan[currX][currY]
        # pan[currX][currY] = 0 
        for x, y in direction :
            dx = currX + x
            dy = currY + y
            
            # if dx > -1 and dx < N and dy > -1 and dy < M and pan[dx][dy] != 0 :
            if dx > -1 and dx < N and dy > -1 and dy < M and pan[dx][dy] == 1 :
                pan[dx][dy] = currVal + 1
                queue.append((dx,dy))
    
print(miroEscape(0,0))
