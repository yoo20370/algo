import sys

N, M = map(int, sys.stdin.readline().split())

for i in range(N) :
    max_val = -1

    max_val = max(max_val, min(list(map(int, sys.stdin.readline().split()))))

print(max_val)
