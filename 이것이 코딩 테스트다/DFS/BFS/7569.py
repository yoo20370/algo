import sys
from collections import deque

col, row, height = map(int, sys.stdin.readline().split())

farm = [[[] for _ in range(row)] for _ in range(height)]

for h in range(height) :
    for r in range(row) :
        farm[h][r].append(list(map(int, sys.stdin.readline().split()))) 

print(farm[1][1][0])
