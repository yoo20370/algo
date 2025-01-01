import sys

listA = list(map(int, sys.stdin.readline().split()))

listA.sort()

print(listA[1])