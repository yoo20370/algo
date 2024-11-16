import sys 
N, M = map(int, input().split())

setA = set()
setB = set()

setA.update(set(map(int, sys.stdin.readline().split())))
setB.update(set(map(int, sys.stdin.readline().split())))

intersect = setA ^ setB

print(len(intersect))