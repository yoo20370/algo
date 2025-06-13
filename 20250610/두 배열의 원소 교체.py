import sys

N, K = map(int, sys.stdin.readline().split())

arrayA = list(map(int, sys.stdin.readline().split()))
arrayB = list(map(int, sys.stdin.readline().split()))

arrayA.sort()
arrayB.sort()


for i in range(K) :
    curr_val = arrayB.pop()
    if curr_val <= arrayA[i] :
        break
    arrayA[i] = curr_val

print(sum(arrayA))