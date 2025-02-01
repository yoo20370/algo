import sys

N, K = map(int, sys.stdin.readline().split())

listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))

listA.sort()
listB.sort(reverse=True)

for i in range(K) :
    if listA[i] < listB[i] :
        listA[i], listB[i] = listB[i], listA[i]
    else :
        break

print(sum(listA))