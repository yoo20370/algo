import sys

N = int(sys.stdin.readline().rstrip())

arr = list()
for i in range(N) :
    arr.append(int(sys.stdin.readline().rstrip()))

def quickSort(arr, left, right) :
    pl = left
    pr = right 
    p = (pl + pr) // 2

    while pl <= pr :
        while arr[pl] > arr[p] :
            pl += 1
        while arr[pr] < arr[p] :
            pr -= 1
        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if left < pr :
        quickSort(arr, left, pr)
    if pl < right :
        quickSort(arr, pl, right)

quickSort(arr, 0, len(arr)-1)
for i in arr :
    print(i, end=" ")