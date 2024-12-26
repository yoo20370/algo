import sys

arr = list()

N = int(sys.stdin.readline().rstrip())

for _ in range(N) :
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()

for item in arr :
    print(item)