import sys

N, M = map(int, sys.stdin.readline().split())

max = 0 
for i in range(N) :
    minVal = min(map(int, sys.stdin.readline().split()))
    if max < minVal :
        max = minVal

print(max)