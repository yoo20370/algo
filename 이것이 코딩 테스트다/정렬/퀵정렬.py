
def quickSort(arr, left, right) :

    pl = left
    pr = right
    p = arr[(left+right) // 2]

    while pl <= pr :
        while arr[pl] < p :
            pl += 1
        while arr[pr] > p :
            pr -= 1
        
        if pl <= pr :
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if left < pr :
        quickSort(arr, left, pr)
    if pl < right :
        quickSort(arr, pl, right)

arr = [3, 2, 4, 1]

quickSort(arr, 0, len(arr)-1)
print(arr)