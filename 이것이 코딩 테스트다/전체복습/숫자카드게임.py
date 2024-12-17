import sys

N, M = map(int, sys.stdin.readline().split())

maxVal = 0

for _ in range(N) :
    cards = list(map(int, sys.stdin.readline().split()))
    minVal = min(cards)
    maxVal = max(maxVal, minVal)

print(maxVal)