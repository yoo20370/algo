import sys

row, col = map(int, sys.stdin.readline().split())

maxValue = 0
for _ in range(row) :
    inputNumberList = list(map(int, sys.stdin.readline().split()))
    minValue = min(inputNumberList)

    maxValue = max(maxValue, minValue)


print(maxValue)

