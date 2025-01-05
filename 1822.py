import sys

def binary_search(arr, key) -> int :
    pl = 0 
    pr = len(arr) - 1

    while pl <= pr :
        mid = (pl + pr) // 2

        if arr[mid] < key :
            pl = mid + 1
        elif arr[mid] > key :
            pr = mid - 1
        else :
            return arr[mid]
        
    return -1 

N, M = map(int, sys.stdin.readline().split())

listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))

listB.sort()

arr = list()
for key in listA :
    result = binary_search(listB, key)
    if result == -1 :
        arr.append(key)

arr.sort()
if len(arr) == 0 :
    print(0)
else :
    print(len(arr))
    for i in arr :
        print(i, end=" ")