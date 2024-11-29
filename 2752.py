import sys

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

for i in arr :
    print(i, end=" ")