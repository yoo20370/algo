import sys

N, M = map(int, sys.stdin.readline().split())

arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()
arr2.sort(reverse=True)

print(arr1)
print(arr2)

for idx in range(M) :
    if arr1[idx] > arr2[idx] :
        break
    arr1[idx], arr2[idx] = arr2[idx], arr1[idx]

print(sum(arr1))