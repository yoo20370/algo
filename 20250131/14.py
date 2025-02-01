arr = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]

def quick_sort(left, right, arr) :

    pl = left
    pr = right
    p = arr[(pl + pr) // 2]

    while arr[pl] < p :
        pl += 1

    while arr[pr] > p :
        pr -= 1

    if pl <= pr :
        arr[pl], arr[pr] = arr[pr], arr[pl]
        pl += 1
        pr -= 1
    
    if left < pr :
        quick_sort(left, pr, arr)
    if pl < right :
        quick_sort(pl, right, arr)
        
quick_sort(0, len(arr)-1, arr)

print(arr)