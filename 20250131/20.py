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
            return mid
    
    return -1 

N = int(sys.stdin.readline().rstrip())

store = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
order = list(map(int, sys.stdin.readline().split()))

store.sort()

for curr in order :
    result = binary_search(store, curr)
    if result != -1 :
        print("yes", end=" ")
    else :
        print("no", end=" ")
