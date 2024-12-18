import sys

N, K = map(int, sys.stdin.readline().split())

firstArr = list(map(int, sys.stdin.readline().split()))
secondArr = list(map(int, sys.stdin.readline().split()))

firstArr.sort()
secondArr.sort(reverse=True)

for idx in range(K) :
    if firstArr[idx] > secondArr[idx] :
        break 
    firstArr[idx] = secondArr[idx]

print(sum(firstArr))