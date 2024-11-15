import sys

def binarySearch(arr, key) :
    pl = 0
    pr = len(arr) - 1

    while pl <= pr :
        mid = (pl + pr) // 2
        if arr[pl] < key :
            pl = mid + 1
        elif key < arr[pr] :
            pr = mid - 1
        else :
            return key
    return -1

N, M = map(int, input().split())

listA = list()
for i in range(N) :
    listA.append(sys.stdin.readline().rstrip())

listA.sort()

resultList = list()
for i in range(M) :
    data = sys.stdin.readline().rstrip()
    
    result = binarySearch(listA, data)
    if result != -1 :
        resultList.append(result)

resultList.sort()

print(len(resultList))
for i in resultList :
    print(i)

