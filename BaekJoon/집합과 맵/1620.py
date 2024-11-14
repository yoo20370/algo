import sys

N, M = map(int, input().split())

listA = [[] for i in range(1000)]

for i in range(N) :
    data = sys.stdin.readline().rstrip()
    hashVal = i // 1000
    listA[hashVal].append([i, data])

print(listA)

# for i in range(M) :

