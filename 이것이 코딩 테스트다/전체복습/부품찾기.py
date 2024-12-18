import sys

N = int(sys.stdin.readline().rstrip())
storeList = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
orderList = list(map(int, sys.stdin.readline().split()))



def binary_search(arr, item) -> str :

    pl = 0 
    pr = len(arr) - 1

    while pl <= pr :
        mid = (pl + pr) // 2
        if arr[mid] < item :
            pl = mid + 1
        elif arr[mid] > item :
            pr = mid - 1
        else :
            return "yes"
    
    return "no"

for item in orderList :
    print(binary_search(storeList, item), end=" ")